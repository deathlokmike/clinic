import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.appointments import Appointments
from app.models.users.roles import Roles
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.personal_data import PersonalData


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str]
    password: Mapped[str]
    registration_date: Mapped[datetime] = mapped_column(
        types.DateTime, default=datetime.utcnow(), nullable=True)
    last_login_date: Mapped[datetime] = mapped_column(
        types.DateTime, default=datetime.utcnow(), nullable=True)
    pd_id: Mapped[int] = mapped_column(ForeignKey("personal_data.id"), nullable=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    role: Mapped["Roles"] = relationship(back_populates="users")
    personal_data: Mapped["PersonalData"] = relationship(back_populates="user")
    appointments: Mapped[list["Appointments"]] = relationship(back_populates="user")
