from app.services.dao.base import BaseDAO
from app.models.schedule import Schedule


class ScheduleDaO(BaseDAO):
    model = Schedule
