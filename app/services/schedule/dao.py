import datetime
from app.services.database import async_session
from app.services.dao.base import BaseDAO
from app.models.schedule import Schedule
from sqlalchemy import select, between, and_


class ScheduleDaO(BaseDAO):
    model = Schedule

    @classmethod
    async def get_available(cls):
        async with async_session() as session:
            query = select(Schedule.start_time, Schedule.end_time).where(
                Schedule.end_time > datetime.datetime.now()
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def check_date(cls, date_time: datetime.datetime) -> bool:
        async with async_session() as session:
            query = select(Schedule.id).where(
                and_(
                    between(date_time, Schedule.start_time, Schedule.end_time),
                    date_time != Schedule.end_time,
                )
            )
            result = await session.execute(query)
            if len(result.scalars().all()) == 0:
                return False
            return True
