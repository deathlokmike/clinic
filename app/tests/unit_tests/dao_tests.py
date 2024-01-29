import datetime
from contextlib import nullcontext as does_not_raise

import pytest

from app.services.appointments.dao import AppointmentsDAO
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
async def test_doctor_appointment(date_time: datetime.datetime, doctor_id: int, res: bool):
    result = await AppointmentsDAO.check_appointment(date_time, doctor_id)
    assert result == res


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
