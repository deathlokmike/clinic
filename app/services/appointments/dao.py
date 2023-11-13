from app.services.dao.base import BaseDAO
from app.models.appointments import Appointments
from app.models.doctors import Doctors
from sqlalchemy import select
from app.services.database import async_session


class AppointmentsDAO(BaseDAO):
    model = Appointments

    @classmethod
    async def get_patient_appointments(cls, patient_id: str) -> dict:
        async with async_session() as session:
            # select a.date_time, a.status, a.result, d.specialization, d.full_name, d.profile_photo_path
            # from appointments a
            # left join doctors d
            #     on a.doctor_id = d.id
            # where patient_id = patient.id

            query = (
                select(
                    Appointments.date_time,
                    Appointments.status,
                    Doctors.specialization,
                    Doctors.full_name,
                    Doctors.profile_photo_path,
                )
                .join(Doctors, Appointments.doctor_id == Doctors.id, isouter=True)
                .where(Appointments.patient_id == patient_id)
            )

            result = await session.execute(query)
            return result.mappings().all()
