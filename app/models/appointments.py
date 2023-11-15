from typing import TYPE_CHECKING

from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, DateTime, Integer

from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.doctors import Doctors
    from app.models.users.patients import Patients
    from app.models.treatments import Treatments


class Appointments(Base):
    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)

    doctor: Mapped["Doctors"] = relationship(back_populates="appointments")
    patient: Mapped["Patients"] = relationship(back_populates="appointments")
