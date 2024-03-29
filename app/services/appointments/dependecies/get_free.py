import datetime

from pydantic import TypeAdapter

from app.services.doctors.dao import DoctorsDAO
from app.services.doctors.schemas import (SAvailableAppointments,
                                          SDoctorWithBookedAppointments,
                                          SDoctorWithFreeAppointments,
                                          SFreeAppointmentsTimeGroupedByDate)
from app.services.schedule.dao import ScheduleDaO


async def get_relevant_schedule(
        start_lunch_break=datetime.time(hour=12),
        end_lunch_break=datetime.time(hour=13),
        step=datetime.timedelta(hours=1),
) -> list[datetime.datetime]:
    schedule = await ScheduleDaO.get_available()
    result = list()
    for s in schedule:
        date: datetime.datetime = s["start_time"]
        while date < s["end_time"]:
            if start_lunch_break > date.time() or date.time() >= end_lunch_break:
                result.append(date)
            date += step
    return result


def _add_appointments_by_date(grouped_appointments: list[SFreeAppointmentsTimeGroupedByDate],
                              appointment: datetime.datetime):
    if (len(grouped_appointments) == 0
            or grouped_appointments[-1].date != appointment.date()):
        grouped_appointments.append(SFreeAppointmentsTimeGroupedByDate(date=appointment.date(), time=list()))
    grouped_appointments[-1].time.append(appointment.time())


def _group_appointments_by_date(appointments: list[datetime.datetime]) -> list[SFreeAppointmentsTimeGroupedByDate]:
    result: list[SFreeAppointmentsTimeGroupedByDate] = list()
    for appointment in appointments:
        _add_appointments_by_date(result, appointment)
    return result


def _add_doctor_by_specialization(
        available_appointments: list[SAvailableAppointments],
        doctor: SDoctorWithBookedAppointments,
        schedule: list[datetime.datetime]
):
    def _add_doctor(_available_appointments: SAvailableAppointments):
        temp_schedule = schedule.copy()
        for a in doctor.appointments:
            try:
                temp_schedule.remove(a.date_time)
            except ValueError:
                pass
        _doctor = SDoctorWithFreeAppointments(
            id=doctor.id,
            experience=doctor.experience,
            personal_data=doctor.user.personal_data,
            free_appointments=_group_appointments_by_date(temp_schedule),
        )
        _available_appointments.doctors.append(_doctor)

    for available_appointment in available_appointments:
        if available_appointment.specialization == doctor.specialization:
            _add_doctor(available_appointment)
            return

    available_appointments.append(
        SAvailableAppointments(specialization=doctor.specialization, doctors=list())
    )
    _add_doctor(available_appointments[-1])


async def get_free_appointments() -> list[SAvailableAppointments]:
    doctors = await DoctorsDAO.get_all_with_booked_appointments()
    schedule: list[datetime.datetime] = await get_relevant_schedule()
    available_appointments: list[SAvailableAppointments] = list()
    for d in doctors:
        d = TypeAdapter(SDoctorWithBookedAppointments).validate_python(d["Doctors"])
        _add_doctor_by_specialization(available_appointments, d, schedule)
    return available_appointments
