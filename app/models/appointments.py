from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.services.database import Base
from app.models.users.doctors import Doctors
from app.models.treatments import Treatments
from uuid import UUID

if TYPE_CHECKING:
    from app.models.users.users import Users


class Appointments(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)

    doctor: Mapped["Doctors"] = relationship(back_populates="appointments")
    user: Mapped["Users"] = relationship(back_populates="appointments")
    treatment: Mapped["Treatments"] = relationship(back_populates="appointment")
