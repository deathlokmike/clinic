from sqlalchemy import select, insert, update

from app.models.users.personal_data import PersonalData
from app.models.users.users import Users
from app.services.base_dao import BaseDAO
from app.services.database import async_session
from app.services.users.schemas import SUserPersonalData


class UsersDaO(BaseDAO):
    model = Users

    @classmethod
    async def get_by_id(cls, model_id: str) -> Users:
        return await cls.get_one_or_none(id=model_id)

    @classmethod
    async def get_personal_data(cls, model_id: str):
        async with async_session() as session:
            user = (
                select(Users)
                .where(Users.id == model_id)
            ).subquery("user")
            query = select(PersonalData).where(PersonalData.id == user.c.pd_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def _update_pd_id(cls, user_id: str, pd_id: int):
        async with async_session() as session:
            query = (
                update(Users)
                .where(Users.id == user_id)
                .ordered_values(
                    (Users.pd_id, pd_id)
                )
            )
            await session.execute(query)
            await session.commit()

    @classmethod
    async def add_full_name(cls, pd: SUserPersonalData) -> int:
        async with async_session() as session:
            query = (
                insert(PersonalData).values(
                    first_name=pd.first_name,
                    second_name=pd.second_name,
                    last_name=pd.last_name,
                    profile_photo_path=pd.profile_photo_path
                ).returning(
                    PersonalData.id
                )
            )
            pd_id = await session.execute(query)
            await session.commit()
            return int(pd_id.mappings().one()["id"])
