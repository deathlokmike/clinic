from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from app.services.database import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users.users import Users


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    users: Mapped[list["Users"]] = relationship(back_populates="role")
