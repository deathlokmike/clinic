from app.models.common import ExtendedUsers
from sqlalchemy.orm import Mapped, relationship


class Patients(ExtendedUsers):
    __tablename__ = 'patients'
