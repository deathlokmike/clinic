from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Date
from datetime import date
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users import Users
    from app.models.appointments import Appointments


class Patients(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    full_name: Mapped[str]
    birth_day: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[bool]
    passport_data: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[str]
    profile_photo_path: Mapped[str]

    user: Mapped["Users"] = relationship(back_populates="patient")
    appointments: Mapped[list["Appointments"]] = relationship(back_populates="patient")
