import datetime

from app.services.schedule.dao import ScheduleDaO
from app.tasks.celery_app import worker


def _insert_new_date_times(start: datetime.datetime, now: datetime.datetime):
    while start < (now + datetime.timedelta(days=31)):
        if start.weekday() < 5:
            ScheduleDaO.insert_new(start.date())
        start += datetime.timedelta(days=1)


def set_actual_schedule():
    now = datetime.datetime.now()
    ScheduleDaO.delete_old(now)
    last_datetime = ScheduleDaO.get_last_datetime()
    if last_datetime:
        start_datetime = last_datetime + datetime.timedelta(days=1)
    else:
        start_datetime = now
    _insert_new_date_times(start_datetime, now)


@worker.task
def set_actual_schedule_task():
    set_actual_schedule()
