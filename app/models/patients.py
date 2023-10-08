from app.models.common import Person

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Patients(Person):
    __tablename__ = 'patients'
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
