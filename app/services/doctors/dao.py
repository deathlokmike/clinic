from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, func, select
from sqlalchemy.orm import joinedload, selectinload, with_loader_criteria

from app.models.appointments import Appointments
from app.models.users.doctors import Doctors
from app.models.users.personal_data import PersonalData
from app.models.users.users import Users
from app.services.base_dao import BaseDAO
from app.services.database import async_session


class DoctorsDAO(BaseDAO):
    model = Doctors

    @classmethod
    async def get_all_with_booked_appointments(cls):
        async with async_session() as session:
            query = (
                select(Doctors)
                .options(joinedload(Doctors.user)
                         .load_only(Users.id)
                         .options(joinedload(Users.personal_data)
                                  .load_only(PersonalData.first_name,
                                             PersonalData.second_name,
                                             PersonalData.last_name,
                                             PersonalData.profile_photo_path)))
                .options(
                    selectinload(Doctors.appointments)
                    .load_only(Appointments.date_time),
                    with_loader_criteria(
                        Appointments,
                        Appointments.date_time > func.now(),
                        Appointments.status != 2
                    ),

                )
                .where(Doctors.resigned == False)
            )
            result = await session.execute(query)
            return jsonable_encoder(result.mappings().all())

    @classmethod
    async def get_by_id(cls, _id: int):
        async with async_session() as session:
            query = (
                select(Doctors.__table__.columns)
                .where(
                    and_(Doctors.id == _id,
                         Doctors.resigned == False)))
            result = await session.execute(query)
            return result.mappings().one_or_none()
