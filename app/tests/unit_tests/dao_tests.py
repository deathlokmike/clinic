import datetime

import pytest
from app.services.schedule.dao import ScheduleDaO
from app.services.schedule.tasks import set_actual_schedule
from app.services.appointments.dao import AppointmentsDAO


# from contextlib import nullcontext as does_not_raise


# @pytest.mark.parametrize(
#     "date_time, res",
#     [
#         (datetime.datetime(year=2023, month=11, day=19, hour=9), False),
#         (datetime.datetime(year=2022, month=11, day=19, hour=9), False),
#         (datetime.datetime(year=2023, month=11, day=23, hour=7), False),
#         (datetime.datetime(year=2023, month=11, day=23, hour=17), False),
#         (datetime.datetime(year=2023, month=11, day=23, hour=16), True),
#         (datetime.datetime(year=2023, month=11, day=24, hour=8), True),
#         (datetime.datetime(year=2023, month=11, day=24, hour=9), True),
#     ],
# )
# async def test_schedule_between(date_time, res: bool):
#     result = await ScheduleDaO.check_date(date_time)
#     assert result == res


@pytest.mark.parametrize(
    "date_time, doctor_id, res",
    [
        (datetime.datetime(year=2023, month=11, day=21, hour=15), 2, False),
        (datetime.datetime(year=2023, month=11, day=21, hour=16), 2, True),
        (datetime.datetime(year=2023, month=11, day=23, hour=10), 5, True),
    ],
)
async def test_doctor_appointment(
        date_time: datetime.datetime, doctor_id: int, res: bool
):
    result = await AppointmentsDAO.check_appointment(date_time, doctor_id)
    assert result == res


# async def test_last_datetime():
#     await set_actual_schedule()
#     await ScheduleDaO.get_all()
#     assert 1 == 1
