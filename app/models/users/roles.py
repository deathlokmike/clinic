from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from app.services.database import Base


class Roles(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
