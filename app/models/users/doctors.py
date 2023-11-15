from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Date, ForeignKey
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.appointments import Appointments
    from app.models.users.personal_data import PersonalData


class Doctors(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True)
    pd_id: Mapped[str] = mapped_column(ForeignKey("personal_data.id"), nullable=False)

    specialization: Mapped[str]  # специализация
    date_employment: Mapped[date] = mapped_column(
        Date, nullable=False
    )  # дата начала работы
    pre_work_experience: Mapped[int]  # предыдущий опыт работы
    resigned: Mapped[bool]  # уволился

    personal_data: Mapped["PersonalData"] = relationship(back_populates="doctor")
    appointments: Mapped[list["Appointments"]] = relationship(back_populates="doctor")
