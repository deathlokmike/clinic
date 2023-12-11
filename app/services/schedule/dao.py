import datetime
from app.services.database import async_session
from app.services.base_dao import BaseDAO
from app.models.schedule import Schedule
from sqlalchemy import select, between, and_, delete, insert, desc


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
    async def delete_old(cls, date_time: datetime.datetime):
        async with async_session() as session:
            query = delete(Schedule).where(Schedule.end_time < date_time)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def insert_new(cls, date: datetime.date):
        start = datetime.datetime(
            year=date.year, month=date.month, day=date.day, hour=8
        )
        end = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=17)
        async with async_session() as session:
            query = insert(Schedule).values(start_time=start, end_time=end)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_last_datetime(cls) -> datetime.datetime | None:
        async with async_session() as session:
            query = select(Schedule.end_time).order_by(desc(Schedule.end_time)).limit(1)
            result = await session.execute(query)
            return result.scalars().one_or_none()
