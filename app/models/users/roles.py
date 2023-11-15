from typing import TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from app.services.database import Base

if TYPE_CHECKING:
    from app.models.users.users import Users


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
