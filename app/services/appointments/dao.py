from app.services.dao.base import BaseDAO
from app.models.appointments import Appointments
from app.models.users.doctors import Doctors
from app.models.users.personal_data import PersonalData
from sqlalchemy import select
from app.services.database import async_session


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
