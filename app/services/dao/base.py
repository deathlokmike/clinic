from app.services.database import async_session

from sqlalchemy import select, insert, delete


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls):
        async with async_session() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def get_by_id(cls, model_id: int):
        return await cls.get_one_or_none(id=model_id)

    @classmethod
    async def insert_value(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_value(cls, **filter_by):
        async with async_session() as session:
            query = delete(cls.model.__table__).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()

