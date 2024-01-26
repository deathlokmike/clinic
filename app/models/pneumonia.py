from sqlalchemy.orm import Mapped, mapped_column

from app.services.database import Base


class Pneumonia(Base):
    __tablename__ = "pneumonia"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)  # Тип
    pathogen: Mapped[str] = mapped_column(nullable=False)  # Патоген
    morbidity: Mapped[float] = mapped_column(nullable=False)  # Частота заболеваемости
    mortality: Mapped[float] = mapped_column(nullable=False)  # Смертность
    severity: Mapped[str] = mapped_column(nullable=False)  # Тяжесть
    symptoms: Mapped[str] = mapped_column(nullable=False)  # Симптомы
