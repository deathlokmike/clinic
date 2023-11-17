import datetime
from app.services.database import async_session
from app.services.dao.base import BaseDAO
from app.models.schedule import Schedule
from sqlalchemy import select


class ScheduleDaO(BaseDAO):
    model = Schedule

    @classmethod
    async def get_available(cls):
        async with async_session() as session:
            query = (
                select(Schedule.start_time, 
                    Schedule.end_time)
                .where(Schedule.end_time > datetime.datetime.now()))
            result = await session.execute(query)
            return result.mappings().all()
