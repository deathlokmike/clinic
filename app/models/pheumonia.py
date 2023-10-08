from sqlalchemy.orm import Mapped, mapped_column

from app.services.database import Base


class PneumoniaTypes(Base):
    __tablename__ = 'pneumonia_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=True)
    pathogen: Mapped[str] = mapped_column(nullable=True)
    morbidity: Mapped[float] = mapped_column(nullable=True)
    mortality: Mapped[float] = mapped_column(nullable=True)
    severity: Mapped[int] = mapped_column(nullable=True)
