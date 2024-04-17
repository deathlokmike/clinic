from celery import Celery
from celery.schedules import crontab

from app.config import settings

worker = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=[
        "app.tasks.scheduled"
    ]
)

worker.conf.beat_schedule = {
    "scheduled": {
        "task": "set_actual_schedule",
        "schedule": crontab(minute='10', hour='0')
    }
}

worker.conf.timezone = "Europe/Moscow"
