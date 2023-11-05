from app.services.dao.base import BaseDAO
from app.models.appointments import Appointments
from app.models.users import Users
from app.models.patients import Patients
from app.models.doctors import Doctors
from sqlalchemy import select
from app.services.database import async_session


class AppointmentsDAO(BaseDAO):
    model = Appointments

    @classmethod
    async def get_patient_appointments(cls, user_id: str) -> dict:
        async with async_session() as session:
            # with patient as(
            #   select p.id 
            #   from patients p left join 
            #   users u on p.user_id=u.id
            # where u.id = user_id);
            patient = (select(
                Patients.id)
                .join(Users, Patients.user_id == Users.id, isouter=True)
                .where(Users.id == user_id)
                ).cte("patient")
            
            # select a.date_time, a.status, a.result, d.specialization, d.full_name, d.profile_photo_path 
            # from appointments a
            # left join doctors d
            #     on a.doctor_id = d.id
            # where patient_id = patient.id

            query = (select(
                Appointments.date_time,
                Appointments.status,
                Doctors.specialization,
                Doctors.full_name,
                Doctors.profile_photo_path)
                .join(Doctors, Appointments.doctor_id == Doctors.id, isouter=True)
                .where(
                    Appointments.patient_id == patient.c.id
                ))


            result = await session.execute(query)
            return result.mappings().all()