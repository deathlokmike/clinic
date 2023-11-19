from fastapi import APIRouter, Depends
from app.models.users.personal_data import PersonalData

from app.services.schedule.dao import ScheduleDaO
from app.services.doctors.dao import DoctorsDAO
from app.services.users.dependencies import get_personal_data
from app.services.appointments.dao import AppointmentsDAO
from app.services.patients.dao import PatientsDAO
from app.services.users.schemas import SExtendedUser
from app.services.appointments.schemas import (
    SAppointmentsWithPatientInfo,
    SNewAppointmentIn,
    SNewAppointmentOut,
)
from app.services.appointments.dependencies import get_free_appointments
from app.services.doctors.schemas import SAvailableAppointments
from pydantic import TypeAdapter
from app.common.exceptions import AppointmentNotAvailableException

router = APIRouter(prefix="/api/appointments", tags=["Записи на прием"])


@router.get("")
async def get_patient_info_and_appointments(
    pd: PersonalData = Depends(get_personal_data),
) -> SAppointmentsWithPatientInfo:
    patient = await PatientsDAO.get_one_or_none(pd_id=pd.id)
    appointments = await AppointmentsDAO.get_patient_appointments(patient_id=patient.id)
    personal_data = TypeAdapter(SExtendedUser).validate_python(pd).model_dump()
    return {"personal_data": personal_data, "appointments": appointments}


@router.get("/available")
async def get_available_appointments(
    available_appointments: list[SAvailableAppointments] = Depends(
        get_free_appointments
    ),
) -> list[SAvailableAppointments]:
    return available_appointments


@router.post("/book")
async def book_appointment(
    new_appointment: SNewAppointmentIn, pd: PersonalData = Depends(get_personal_data)
) -> SNewAppointmentOut:
    if new_appointment.date_time.minute != 0 or new_appointment.date_time.second != 0:
        raise AppointmentNotAvailableException

    schedule_check: bool = await ScheduleDaO.check_date(new_appointment.date_time)
    if not schedule_check:
        raise AppointmentNotAvailableException

    appointment_check: bool = await AppointmentsDAO.check_appointment(
        new_appointment.date_time, new_appointment.doctor_id
    )
    if not appointment_check:
        raise AppointmentNotAvailableException

    doctor_pd = await DoctorsDAO.get_personal_data(new_appointment.doctor_id)
    if not doctor_pd:
        raise AppointmentNotAvailableException

    patient = await PatientsDAO.get_one_or_none(pd_id=pd.id)

    appointment = await AppointmentsDAO.add(patient.id, new_appointment)
    if not appointment:
        raise AppointmentNotAvailableException

    return SNewAppointmentOut(
        full_name=doctor_pd.full_name,
        date_time=appointment.date_time,
        status=appointment.status,
    )
