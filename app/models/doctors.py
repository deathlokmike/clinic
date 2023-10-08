from app.models.common import Person
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Date


class Doctors(Person):
    __tablename__ = 'doctors'
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    specialization: Mapped[str]
    date_employment: Mapped[date] = mapped_column(Date, nullable=False)
    length_service: Mapped[int]
