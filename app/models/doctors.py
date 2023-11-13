from typing import TYPE_CHECKING
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Date, ForeignKey
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.appointments import Appointments
    from app.models.users import Users
    from app.models.schedule import Schedule


class Doctors(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    full_name: Mapped[str]
    birth_day: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[bool]
    passport_data: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[str]
    profile_photo_path: Mapped[str]

    specialization: Mapped[str]  # специализация
    date_employment: Mapped[date] = mapped_column(
        Date, nullable=False
    )  # дата начала работы
    pre_work_experience: Mapped[int]  # предыдущий опыт работы
    resigned: Mapped[bool]  # уволился

    user: Mapped["Users"] = relationship(back_populates="doctor")
    appointments: Mapped[list["Appointments"]] = relationship(back_populates="doctor")
    schedule: Mapped[list["Schedule"]] = relationship(back_populates="doctor")
