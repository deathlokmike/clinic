from app.services.dao.base import BaseDAO
from app.models.users import Users


class UsersDaO(BaseDAO):
    model = Users

    @classmethod
    async def get_by_id(cls, model_id: str):
        return await cls.get_one_or_none(id=model_id)
