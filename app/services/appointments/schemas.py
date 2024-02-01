import datetime

from pydantic import BaseModel

from app.services.doctors.schemas import SDoctorWithPersonalData
from app.services.users.schemas import SUserPersonalData


class SUserAppointment(BaseModel):
    date_time: datetime.datetime
    status: int
    doctor: SDoctorWithPersonalData


class SPatientInfoWithAppointments(BaseModel):
    personal_data: SUserPersonalData
    appointments: list[SUserAppointment]


class SNewAppointmentIn(BaseModel):
    doctor_id: int
    date_time: datetime.datetime


class SNewAppointmentOut(BaseModel):
    date_time: datetime.datetime
    status: int
