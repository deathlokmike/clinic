from sqlalchemy import delete, insert, select

from app.services.database import Base, async_session


class BaseDAO:
    model: Base = None

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
    async def add(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_value(cls, **filter_by):
        async with async_session() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
