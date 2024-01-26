from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.users import Users


class PersonalData(Base):
    __tablename__ = "personal_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    second_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    birth_day: Mapped[date] = mapped_column(Date, nullable=True)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=True)
    passport_data: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    profile_photo_path: Mapped[str] = mapped_column(String, nullable=True)

    user: Mapped["Users"] = relationship(back_populates="personal_data")

    @hybrid_property
    def full_name(self) -> str:
        return self.last_name + " " + self.first_name + " " + self.second_name
