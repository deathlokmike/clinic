import datetime

from sqlalchemy import and_, between, delete, desc, insert, select

from app.logger import logger
from app.models.schedule import Schedule
from app.services.base_dao import BaseDAO
from app.services.database import async_session, sync_session


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
    async def check_availability_date(cls, date_time: datetime.datetime) -> bool:
        async with async_session() as session:
            query = select(Schedule.start_time).where(
                and_(
                    between(date_time, Schedule.start_time, Schedule.end_time),
                    date_time != Schedule.end_time,
                )
            )
            result = await session.execute(query)
            if len(result.scalars().all()) == 0:
                return False
            return True

    @classmethod
    def delete_old(cls, datetime_now: datetime.datetime):
        with sync_session() as session:
            query = delete(Schedule).where(Schedule.end_time < datetime_now)
            logger.info("Delete old schedule records", extra={
                "date_time": datetime_now,
                "query": query,
            })
            session.execute(query)
            session.commit()

    @classmethod
    def insert_new(cls, date: datetime.date):
        start = datetime.datetime(
            year=date.year, month=date.month, day=date.day, hour=8
        )
        end = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=17)
        with sync_session() as session:
            query = insert(Schedule).values(start_time=start, end_time=end)
            logger.info("Insert new schedule records", extra={
                "start_time": start,
                "end_time": end,
                "query": query,
            })
            session.execute(query)
            session.commit()

    @classmethod
    def get_last_datetime(cls) -> datetime.datetime | None:
        with sync_session() as session:
            query = select(Schedule.end_time).order_by(desc(Schedule.end_time)).limit(1)
            result = session.execute(query)
            return result.scalars().one_or_none()
