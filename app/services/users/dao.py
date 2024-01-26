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
    async def get_personal_data_by_id(cls, model_id: str):
        async with async_session() as session:
            query = (
                select(
                    Users.email,
                    PersonalData.__table__.columns,
                    PersonalData.full_name
                ).
                join(PersonalData, Users.id == PersonalData.user_id, isouter=True).
                where(Users.id == model_id)
            )
            result = await session.execute(query)
            return result.mappings().one_or_none()

