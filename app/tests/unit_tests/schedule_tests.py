import datetime

import pytest
from freezegun import freeze_time
from sqlalchemy import select

from app.models.schedule import Schedule
from app.services.database import async_session
from app.services.schedule.dao import ScheduleDaO


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "datetime_, count",
    [
        ("2023-11-04 20:40:32", 12),
        ("2023-11-15 15:40:32", 12),
        ("2023-11-15 20:40:32", 11),
        ("2023-11-15 16:00:00", 12),
        ("2023-11-15 17:00:00", 11),
        ("2023-11-27 10:40:32", 4),
    ],
)
async def test_available_count(datetime_: str, count: int):
    with freeze_time(datetime_):
        res = await ScheduleDaO.get_available()
        assert len(res) == count


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "datetime_, count",
    [
        ("2023-12-04 20:40:32", 12),
        ("2023-11-04 20:40:32", 0),
    ],
)
async def test_delete_old_records(datetime_: str, count: int, return_schedule_to_source):
    async def get_schedule():
        async with async_session() as session:
            query = select(Schedule)
            result = await session.execute(query)
            return result.mappings().all()

    with freeze_time(datetime_):
        now = datetime.datetime.now()
        before = await get_schedule()
        ScheduleDaO.delete_old(now)
        after = await get_schedule()
        assert len(before) - len(after) == count


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "date_time, flag",
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
async def test_schedule_between(date_time, flag: bool):
    result = await ScheduleDaO.check_availability_date(date_time)
    assert result == flag
