import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, insert, select
from sqlalchemy.orm import joinedload, selectinload

from app.models.appointments import Appointments
from app.models.users.doctors import Doctors
from app.models.users.personal_data import PersonalData
from app.models.users.users import Users
from app.services.appointments.schemas import SNewAppointmentIn
from app.services.base_dao import BaseDAO
from app.services.database import async_session


class AppointmentsDAO(BaseDAO):
    model = Appointments

    @classmethod
    async def get_patient_appointments(cls, user_id: str):
        async with async_session() as session:
            query = (
                select(Users)
                .options(
                    joinedload(Users.personal_data)
                    .load_only(PersonalData.first_name,
                               PersonalData.second_name,
                               PersonalData.last_name,
                               PersonalData.profile_photo_path))
                .options(
                    selectinload(Users.appointments)
                    .load_only(Appointments.date_time,
                               Appointments.status)
                    .options(
                        joinedload(Appointments.doctor)
                        .load_only(Doctors.specialization)
                        .options(
                            joinedload(Doctors.user)
                            .load_only(Users.id)
                            .options(
                                joinedload(Users.personal_data)
                                .load_only(PersonalData.first_name,
                                           PersonalData.second_name,
                                           PersonalData.last_name,
                                           PersonalData.profile_photo_path))))
                ).where(Users.id == user_id)
            )
            result = await session.execute(query)
            return jsonable_encoder(result.mappings().first())

    @classmethod
    async def add(cls, patient_id: int, new_appointment: SNewAppointmentIn):
        async with async_session() as session:
            query = (
                insert(Appointments)
                .values(
                    patient_id=patient_id,
                    doctor_id=new_appointment.doctor_id,
                    date_time=new_appointment.date_time,
                    status=0,
                )
                .returning(
                    Appointments.date_time,
                    Appointments.status,
                )
            )
            new_appointment = await session.execute(query)
            await session.commit()
            return new_appointment.mappings().one()

    @classmethod
    async def is_not_exist(cls, date_time: datetime.datetime, doctor_id: int) -> bool:
        async with async_session() as session:
            query = select(Appointments).where(
                and_(
                    Appointments.date_time == date_time,
                    Appointments.doctor_id == doctor_id,
                    Appointments.status != 3,
                )
            )
            result = await session.execute(query)
            if len(result.scalars().all()) != 0:
                return False
            return True
