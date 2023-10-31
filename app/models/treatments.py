from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String, DateTime

from app.services.database import Base


class Treatments(Base):
    __tablename__ = 'treatments'

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"), nullable=False)
    complaints: Mapped[str] = mapped_column(String, nullable=True)
    examinations: Mapped[str] = mapped_column(String, nullable=True)
    diagnosis: Mapped[int] = mapped_column(String, nullable=True)
    appointment: Mapped[datetime] = mapped_column(DateTime, nullable=False)
