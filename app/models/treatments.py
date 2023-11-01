from datetime import
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, String

from app.services.database import Base


class Treatments(Base):
    __tablename__ = 'treatments'

    id: Mapped[int] = mapped_column(primary_key=True)
    appointment_id: Mapped[int] = mapped_column(ForeignKey("appointments.id"), nullable=False)
    complaints: Mapped[str] = mapped_column(String, nullable=True)
    examinations: Mapped[str] = mapped_column(String, nullable=True)
    diagnosis: Mapped[int] = mapped_column(String, nullable=True)
