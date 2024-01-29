from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.services.database import Base

if TYPE_CHECKING:
    from app.models.appointments import Appointments


class Treatments(Base):
    __tablename__ = "treatments"

    id: Mapped[int] = mapped_column(primary_key=True)
    appointment_id: Mapped[int] = mapped_column(ForeignKey("appointments.id"), nullable=False)
    complaints: Mapped[str] = mapped_column(String, nullable=True)
    examinations: Mapped[str] = mapped_column(String, nullable=True)
    diagnosis: Mapped[int] = mapped_column(String, nullable=True)
    appointment: Mapped["Appointments"] = relationship(back_populates="treatment")

