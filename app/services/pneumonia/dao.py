from app.services.dao.base import BaseDAO
from app.models.pneumonia import Pneumonia
from app.services.pneumonia.schemas import SPneumonia
from app.services.database import async_session
from sqlalchemy import update


class PneumoniaDAO(BaseDAO):
    model = Pneumonia

    @classmethod
    async def update_values(cls, id_: int, pneumonia: SPneumonia):
        async with (async_session() as session):
            query = update(cls.model
                           ).where(cls.model.id == id_
                                   ).ordered_values(
                (cls.model.type, pneumonia.type),
                (cls.model.pathogen, pneumonia.pathogen),
                (cls.model.morbidity, pneumonia.morbidity),
                (cls.model.mortality, pneumonia.mortality),
                (cls.model.severity, pneumonia.severity),
                (cls.model.symptoms, pneumonia.symptoms)
            )
            await session.execute(query)
            await session.commit()
