import asyncio
import datetime

from app.logger import logger
from app.services.schedule.dao import ScheduleDaO


async def _insert_new_date_times(start: datetime.datetime, now: datetime.datetime):
    while start < (now + datetime.timedelta(days=31)):
        if start.weekday() < 5:
            await ScheduleDaO.insert_new(start.date())
        start += datetime.timedelta(days=1)


async def _sleep_until_end_day(now: datetime.datetime):
    end = datetime.datetime(
        year=now.year, month=now.month, day=now.day, hour=23, minute=59, second=59
    )
    logger.info("Sleep until the end of the day", extra={
        "seconds": (end - now).seconds + 1
    })
    await asyncio.sleep((end - now).seconds + 1)


async def set_actual_schedule():
    while True:
        now = datetime.datetime.now()
        await ScheduleDaO.delete_old(now)
        last_datetime = await ScheduleDaO.get_last_datetime()
        if last_datetime:
            start_datetime = last_datetime + datetime.timedelta(days=1)
        else:
            start_datetime = now
        await _insert_new_date_times(start_datetime, now)
        await _sleep_until_end_day(now)
