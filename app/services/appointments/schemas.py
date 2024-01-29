from datetime import datetime

from pydantic import BaseModel

from app.services.users.schemas import SExtendedUser


class SUserAppointment(BaseModel):
    date_time: datetime
    status: int
    specialization: str
    full_name: str
    profile_photo_path: str


class SAppointmentsWithPatientInfo(BaseModel):
    patient: SExtendedUser
    appointments: list[SUserAppointment]


class SBookedAppointment(BaseModel):
    date_time: datetime


class SNewAppointmentIn(BaseModel):
    doctor_id: int
    date_time: datetime


class SNewAppointmentOut(BaseModel):
    date_time: datetime
    status: int
