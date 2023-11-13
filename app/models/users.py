from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sqlalchemy import types, ForeignKey

import uuid

from app.services.database import Base

if TYPE_CHECKING:
    from app.models.doctors import Doctors
    from app.models.patients import Patients
    from app.models.roles import Roles


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid.uuid4
    )

    email: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    doctor: Mapped["Doctors"] = relationship(back_populates="user")
    patient: Mapped["Patients"] = relationship(back_populates="user")
    role: Mapped["Roles"] = relationship(back_populates="users")
