import datetime

from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from app.common.exceptions import AppointmentNotAvailableException
from app.models.users.personal_data import PersonalData
from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.dependencies import get_free_appointments
from app.services.appointments.schemas import (SNewAppointmentIn,
                                               SNewAppointmentOut,
                                               SPatientInfoWithAppointments)
from app.services.doctors.dao import DoctorsDAO
from app.services.doctors.schemas import SAvailableAppointments
from app.services.schedule.dao import ScheduleDaO
from app.services.users.dependencies import get_personal_data
from app.services.users.schemas import SExtendedUserData

router = APIRouter(prefix="/api/appointments", tags=["Записи на прием"])


@router.get("")
async def get_patient_info_and_appointments(
    pd: PersonalData = Depends(get_personal_data),
) -> SPatientInfoWithAppointments:
    patient = None
    appointments = await AppointmentsDAO.get_patient_appointments(patient_id=patient.id)
    personal_data = TypeAdapter(SExtendedUserData).validate_python(pd).model_dump()
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
    appointment_check: bool = await AppointmentsDAO.is_not_exist(
        appointment.date_time, appointment.doctor_id
    )
    if not appointment_check:
        raise AppointmentNotAvailableException


async def _check_doctor_existence(_id: int):
    doctor_pd = await DoctorsDAO.get_by_id(_id)
    if not doctor_pd:
        raise AppointmentNotAvailableException


async def _add_new_appointment(patient_id, new_appointment: SNewAppointmentIn):
    appointment = await AppointmentsDAO.add(patient_id, new_appointment)
    if appointment:
        return appointment
    raise AppointmentNotAvailableException


@router.post("/book")
async def book_appointment(new_appointment: SNewAppointmentIn) -> SNewAppointmentOut:
    new_appointment.date_time = _convert_date_time(new_appointment.date_time)
    _check_hours_and_minutes(new_appointment.date_time)
    await _check_date_time_is_in_schedule(new_appointment.date_time)
    await _check_appointment_dont_exist(new_appointment)
    await _check_doctor_existence(new_appointment.doctor_id)
    patient = None
    appointment = await _add_new_appointment(patient.id, new_appointment)
    return SNewAppointmentOut(
        date_time=appointment.date_time,
        status=appointment.status,
    )
