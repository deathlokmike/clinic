from app.models.appointments import Appointments
from app.services.dao.base import BaseDAO
from app.models.users.doctors import Doctors
from app.services.dao.base import BaseDAO
from sqlalchemy import select, func
from app.services.database import async_session
from sqlalchemy.orm import with_loader_criteria, joinedload, selectinload
from fastapi.encoders import jsonable_encoder


class DoctorsDAO(BaseDAO):
    model = Doctors

    @classmethod
    async def get_all_with_booked_appointments(cls):
        async with async_session() as session:
            query = (
                select(Doctors)
                .options(joinedload(Doctors.personal_data))
                .options(
                    selectinload(Doctors.appointments),
                    with_loader_criteria(
                        Appointments, Appointments.date_time > func.now()
                    ),
                )
                .where(Doctors.resigned == False)
            )

            result = await session.execute(query)
            return jsonable_encoder(result.scalars().all())
