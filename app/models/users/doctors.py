from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.services.database import Base
from uuid import UUID

if TYPE_CHECKING:
    from app.models.appointments import Appointments


class Doctors(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    specialization: Mapped[str]  # специализация
    date_employment: Mapped[date] = mapped_column(
        Date, nullable=False
    )  # дата начала работы
    pre_work_experience: Mapped[int]  # предыдущий опыт работы
    resigned: Mapped[bool]  # уволился

    appointments: Mapped[list["Appointments"]] = relationship(back_populates="doctor")
