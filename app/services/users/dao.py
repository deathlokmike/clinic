from app.services.dao.base import BaseDAO
from app.models.users import Users


class UsersDaO(BaseDAO):
    model = Users
