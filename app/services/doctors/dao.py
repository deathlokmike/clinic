from app.services.dao.base import BaseDAO
from app.models.users.doctors import Doctors
from app.services.dao.base import BaseDAO
from app.models.appointments import Appointments
from sqlalchemy.orm import selectinload
from sqlalchemy import select, between
from app.services.database import async_session
from datetime import date, datetime, time
from fastapi.encoders import jsonable_encoder


class DoctorsDAO(BaseDAO):
    model = Doctors

    @classmethod
    async def get_busy(cls, date: date):
        async with async_session() as session:
            # select doctor_id, date_time from appointments
            # where date_time between '2023-11-19 08:00:00' and '2023-11-19 17:00:00'
            query = (
                select(Doctors)
                .options(selectinload(Doctors.appointments))
            )
            res = await session.execute(query)
            return jsonable_encoder(res.scalars().all())
            
    # @classmethod
    # async def get_busy(cls, date: date):
    #     async with async_session() as session:
    #         # select doctor_id, date_time from appointments
    #         # where date_time between '2023-11-19 08:00:00' and '2023-11-19 17:00:00'
    #         query = (
    #             select(Doctors)
    #             .join(Doctors.schedule)
    #             .options(selectinload(Doctors.schedule))
    #             .where(
    #                 between(
    #                     Appointments.date_time,
    #                     datetime.combine(date, time(hour=8)),
    #                     datetime.combine(date, time(hour=17)),
    #                 )
    #             )
    #         )
    #         res = await session.execute(query)
    #         print(jsonable_encoder(res.scalars().all()))
