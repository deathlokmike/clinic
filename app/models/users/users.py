from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sqlalchemy import types, ForeignKey

import uuid

from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.personal_data import PersonalData
    from app.models.users.roles import Roles


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        types.Uuid, primary_key=True, default=uuid.uuid4
    )

    email: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    personal_data: Mapped["PersonalData"] = relationship(back_populates="user")
