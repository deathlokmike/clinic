from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from app.services.database import Base


class Schedule(Base):
    __tablename__ = "schedule"
    start_time: Mapped[datetime] = mapped_column(DateTime, primary_key=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
