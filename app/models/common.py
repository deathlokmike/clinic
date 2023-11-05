from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Date, ForeignKey
from datetime import date
from app.services.database import Base


class ExtendedUsers(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    full_name: Mapped[str]
    birth_day: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[bool]
    passport_data: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[str]
    profile_photo_path: Mapped[str]
