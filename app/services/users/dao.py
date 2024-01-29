from sqlalchemy import select

from app.models.users.personal_data import PersonalData
from app.models.users.users import Users
from app.services.base_dao import BaseDAO
from app.services.database import async_session


class UsersDaO(BaseDAO):
    model = Users

    @classmethod
    async def get_by_id(cls, model_id: str):
        return await cls.get_one_or_none(id=model_id)

    @classmethod
    async def get_personal_data(cls, model_id: str):
        async with (async_session() as session):
            user = (
                select(Users)
                .where(Users.id == model_id)
            ).subquery("user")
            query = select(PersonalData).where(PersonalData.id == user.c.pd_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()
