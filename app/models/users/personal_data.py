from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import ForeignKey, Date, String
from datetime import date
from app.services.database import Base
from sqlalchemy.ext.hybrid import hybrid_property

if TYPE_CHECKING:
    from app.models.users.users import Users
    from app.models.users.doctors import Doctors
    from app.models.users.patients import Patients


class PersonalData(Base):
    __tablename__ = "personal_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    first_name: Mapped[str]
    second_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str]
    birth_day: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[bool]
    passport_data: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[str]
    profile_photo_path: Mapped[str]

    user: Mapped["Users"] = relationship(back_populates="personal_data")
    doctor: Mapped["Doctors"] = relationship(back_populates="personal_data")
    patient: Mapped["Patients"] = relationship(back_populates="personal_data")

    @hybrid_property
    def full_name(self) -> str:
        return self.last_name + " " + self.first_name + " " + self.second_name
