from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Date
from datetime import date
from app.services.database import Base


class Person(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]
    birth_day: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[bool]
    passport_data: Mapped[str]
    address: Mapped[str]
    phone_number: Mapped[str]
    image_path: Mapped[str]
