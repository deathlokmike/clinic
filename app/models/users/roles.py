from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.services.database import Base


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
