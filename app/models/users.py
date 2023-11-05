from sqlalchemy.orm import mapped_column, Mapped, relationship

from sqlalchemy import types

import uuid

from app.services.database import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str]
    password: Mapped[str]
    role: Mapped[int]
