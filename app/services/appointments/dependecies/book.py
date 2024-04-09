import datetime

from app.common.exceptions import AppointmentNotAvailableException
from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.schemas import (SNewAppointmentIn,
                                               SNewAppointmentOut)
from app.services.doctors.dao import DoctorsDAO
from app.services.schedule.dao import ScheduleDaO


def _convert_date_time(date_time: datetime.datetime) -> datetime.datetime:
    return date_time.replace(tzinfo=None) + datetime.timedelta(hours=3)


def _check_hours_and_minutes(date_time: datetime.datetime):
    if date_time.minute != 0 or date_time.second != 0:
        raise AppointmentNotAvailableException


async def _check_date_time_is_in_schedule(date_time: datetime.datetime):
    schedule_check: bool = await ScheduleDaO.check_availability_date(date_time)
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


async def _add_new_appointment(user_id: str, new_appointment: SNewAppointmentIn):
    appointment = await AppointmentsDAO.add_new(user_id, new_appointment)
    if appointment:
        return appointment
    raise AppointmentNotAvailableException


async def book_new_appointment(user_id, new_appointment: SNewAppointmentIn) -> SNewAppointmentOut:
    new_appointment.date_time = _convert_date_time(new_appointment.date_time)
    _check_hours_and_minutes(new_appointment.date_time)
    await _check_date_time_is_in_schedule(new_appointment.date_time)
    await _check_appointment_dont_exist(new_appointment)
    await _check_doctor_existence(new_appointment.doctor_id)
    appointment = await _add_new_appointment(user_id, new_appointment)
    return SNewAppointmentOut(
        date_time=appointment.date_time,
        status=appointment.status,
    )
