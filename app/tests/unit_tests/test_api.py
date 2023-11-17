import datetime
from app.services.schedule.dao import ScheduleDaO
from app.services.doctors.dao import DoctorsDAO
from app.services.doctors.schemas import (
    SDoctorWithAppointment,
    SFreeAppointments,
    SDoctorWithFreeAppointments,
)
from pydantic import TypeAdapter


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


def add_doctor_by_specialization(
    free_appointments: list[SFreeAppointments],
    doctor: SDoctorWithAppointment,
    schedule: list[datetime.datetime],
):
    def _add_doctor(_free_appointment: SFreeAppointments):
        temp_schedule = schedule.copy()
        for a in doctor.appointments:
            temp_schedule.remove(a.date_time)
        _doctor = SDoctorWithFreeAppointments(
            full_name=doctor.personal_data.full_name,
            experience=doctor.experience,
            free_appointments=temp_schedule,
        )
        _free_appointment.doctors.append(_doctor)

    for free_appointment in free_appointments:
        if free_appointment.specialization == doctor.specialization:
            _add_doctor(free_appointment)
            return

    free_appointments.append(
        SFreeAppointments(specialization=doctor.specialization, doctors=list())
    )
    _add_doctor(free_appointments[-1])


async def test_available_appointments():
    doctors = await DoctorsDAO.get_all_with_booked_appointments()
    schedule: list[datetime.datetime] = await get_relevant_schedule()
    free_appointments: list[SFreeAppointments] = list()
    for d in doctors:
        d = TypeAdapter(SDoctorWithAppointment).validate_python(d)
        add_doctor_by_specialization(free_appointments, d, schedule)
    assert 1 == 1
