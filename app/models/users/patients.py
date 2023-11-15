from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.personal_data import PersonalData
    from app.models.appointments import Appointments


class Patients(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    pd_id: Mapped[str] = mapped_column(ForeignKey("personal_data.id"), nullable=False)

    personal_data: Mapped["PersonalData"] = relationship(back_populates="patient")
    appointments: Mapped[list["Appointments"]] = relationship(back_populates="patient")
