import datetime
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


def _convert_date_time(date_time: datetime.datetime) -> datetime.datetime:
    return date_time.replace(tzinfo=None) + datetime.timedelta(hours=3)


def _check_hours_and_minutes(date_time: datetime.datetime):
    if date_time.minute != 0 or date_time.second != 0:
        raise AppointmentNotAvailableException


async def _check_date_time_is_in_schedule(date_time: datetime.datetime):
    schedule_check: bool = await ScheduleDaO.check_date(date_time)
    if not schedule_check:
        raise AppointmentNotAvailableException


async def _check_appointment_dont_exist(appointment: SNewAppointmentIn):
    appointment_check: bool = await AppointmentsDAO.check_appointment(
        appointment.date_time, appointment.doctor_id
    )
    if not appointment_check:
        raise AppointmentNotAvailableException


async def _get_doctor_personal_data(_id: int):
    doctor_pd = await DoctorsDAO.get_personal_data(_id)
    if not doctor_pd:
        raise AppointmentNotAvailableException
    return doctor_pd


async def _add_new_appointment(patient_id, new_appointment: SNewAppointmentIn):
    appointment = await AppointmentsDAO.add(patient_id, new_appointment)
    if not appointment:
        raise AppointmentNotAvailableException
    return appointment


@router.post("/book")
async def book_appointment(
    new_appointment: SNewAppointmentIn, pd: PersonalData = Depends(get_personal_data)
) -> SNewAppointmentOut:
    new_appointment.date_time = _convert_date_time(new_appointment.date_time)
    _check_hours_and_minutes(new_appointment.date_time)
    await _check_date_time_is_in_schedule(new_appointment.date_time)
    await _check_appointment_dont_exist(new_appointment)
    doctor_pd = await _get_doctor_personal_data(new_appointment.doctor_id)
    patient = await PatientsDAO.get_one_or_none(pd_id=pd.id)
    appointment = await _add_new_appointment(patient.id, new_appointment)
    return SNewAppointmentOut(
        full_name=doctor_pd.full_name,
        date_time=appointment.date_time,
        status=appointment.status,
    )
