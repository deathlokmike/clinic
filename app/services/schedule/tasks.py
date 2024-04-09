import asyncio
import datetime

from app.logger import logger
from app.services.schedule.dao import ScheduleDaO


async def _insert_new_date_times(start: datetime.datetime, now: datetime.datetime):
    while start < (now + datetime.timedelta(days=31)):
        if start.weekday() < 5:
            await ScheduleDaO.insert_new(start.date())
        start += datetime.timedelta(days=1)


def _get_sleep_time_in_sec(now: datetime.datetime) -> int:
    end = datetime.datetime(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=23,
        minute=59,
        second=59
    )
    return (end - now).seconds + 1


async def _sleep_until_end_day(sleep_time_sec: int):
    logger.info("Sleep until the end of the day", extra={
        "seconds": sleep_time_sec
    })
    await asyncio.sleep(sleep_time_sec)


async def _set_actual_schedule(now: datetime.datetime):
    await ScheduleDaO.delete_old(now)
    last_datetime = await ScheduleDaO.get_last_datetime()
    if last_datetime:
        start_datetime = last_datetime + datetime.timedelta(days=1)
    else:
        start_datetime = now
    await _insert_new_date_times(start_datetime, now)


async def start_schedule_task():
    while True:
        now = datetime.datetime.now()
        await _set_actual_schedule(now)
        time_ = _get_sleep_time_in_sec(now)
        await _sleep_until_end_day(time_)
