import datetime

import pytest
from pydantic import TypeAdapter

from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.schemas import SPatientInfoWithAppointments
from app.services.schedule.dao import ScheduleDaO
from app.services.users.dao import PersonalData, UsersDaO


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "date_time, res",
    [
        (datetime.datetime(year=2023, month=11, day=19, hour=9), False),
        (datetime.datetime(year=2022, month=11, day=19, hour=9), False),
        (datetime.datetime(year=2023, month=11, day=23, hour=7), False),
        (datetime.datetime(year=2023, month=11, day=23, hour=17), False),
        (datetime.datetime(year=2023, month=11, day=23, hour=16), True),
        (datetime.datetime(year=2023, month=11, day=24, hour=8), True),
        (datetime.datetime(year=2023, month=11, day=24, hour=9), True),
    ],
)
async def test_schedule_between(date_time, res: bool):
    result = await ScheduleDaO.check_date(date_time)
    assert result == res


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "date_time, doctor_id, res",
    [
        (datetime.datetime(year=2023, month=11, day=21, hour=15), 2, False),
        (datetime.datetime(year=2023, month=11, day=21, hour=16), 2, True),
        (datetime.datetime(year=2023, month=11, day=22, hour=10), 5, True),
    ],
)
async def test_check_available_appointment(date_time: datetime.datetime, doctor_id: int, res: bool):
    result = await AppointmentsDAO.is_not_exist(date_time, doctor_id)
    assert result == res


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_id, count_appointments",
    [
        ("982eeb52-667c-4acb-9d83-18d7d48f518a", 4),
        ("95291318-f3fa-4f0f-b3a0-8908bfe391b6", 2),
        ("2a4e3522-f10f-4fdf-a714-3e58f451c92e", 1),
        ("5632918c-135b-4c49-8af5-89ed75158fb1", 0)
    ],
)
async def test_patient_appointment(user_id: str, count_appointments: int):
    raw = await AppointmentsDAO.get_patient_appointments(user_id)
    user_with_appointments: SPatientInfoWithAppointments = (
        TypeAdapter(SPatientInfoWithAppointments).validate_python(raw["Users"]))
    assert len(user_with_appointments.appointments) == count_appointments


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "model_id, phone_number",
    [
        ("f68d50db-f10a-48b4-acb1-8fae183cac3a", "79012345678"),
        ("395ed07f-f6eb-4e74-867a-ae6498bc2f2f", "79956789012"),
        ("1dd85ba2-132b-496a-8a32-c7428e842417", "79923456789"),
    ],
)
async def test_personal_data(model_id: str, phone_number: int):
    result = await UsersDaO.get_personal_data(model_id=model_id)
    pd: PersonalData = result["PersonalData"]
    assert pd.phone_number == phone_number
