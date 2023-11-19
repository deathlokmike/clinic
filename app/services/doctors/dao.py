import datetime
from app.models.appointments import Appointments
from app.models.users.personal_data import PersonalData
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
        
    @classmethod
    async def get_personal_data(cls, doctor_id: int):
        async with async_session() as session:
            query = (
                select(Doctors.id,
                       PersonalData.full_name)
                .join(PersonalData, Doctors.pd_id == PersonalData.id)
                .where(Doctors.id == doctor_id)
            )
            result = await session.execute(query)
            return result.mappings().one()
