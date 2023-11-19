from app.services.dao.base import BaseDAO
from app.models.appointments import Appointments
from app.models.users.doctors import Doctors
from app.models.users.personal_data import PersonalData
from sqlalchemy import select, insert, and_
from app.services.database import async_session
from app.services.appointments.schemas import SNewAppointmentIn
import datetime


class AppointmentsDAO(BaseDAO):
    model = Appointments

    @classmethod
    async def get_patient_appointments(cls, patient_id: int):
        async with async_session() as session:
            # select a.date_time, a.status, a.result, d.specialization, d.full_name, d.profile_photo_path
            # from appointments a
            # left join doctors d
            #     on a.doctor_id = d.id
            # left join personal_data pd
            #     of d.pd_id = pd.id
            # where patient_id = patient.id

            query = (
                select(
                    Appointments.date_time,
                    Appointments.status,
                    Doctors.specialization,
                    PersonalData.full_name,
                    PersonalData.profile_photo_path,
                )
                .join(Doctors, Appointments.doctor_id == Doctors.id, isouter=True)
                .join(PersonalData, Doctors.pd_id == PersonalData.id)
                .where(Appointments.patient_id == patient_id)
            )

            result = await session.execute(query)
            return result.mappings().all()

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
    async def check_appointment(
        cls, date_time: datetime.datetime, doctor_id: int
    ) -> bool:
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
