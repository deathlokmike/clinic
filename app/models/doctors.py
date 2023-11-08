from app.models.common import ExtendedUsers

from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date


class Doctors(ExtendedUsers):
    __tablename__ = 'doctors'
    specialization: Mapped[str]  # специализация
    date_employment: Mapped[date] = mapped_column(Date, nullable=False)  # дата начала работы
    pre_work_experience: Mapped[int]  # предыдущий опыт работы
    resigned: Mapped[bool] # уволился

