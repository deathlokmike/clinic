from pydantic import BaseModel
from datetime import datetime

from tomlkit import date
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


class SFreeDoctorsAppointments(BaseModel):
    full_name: str
    experience: int
    free_appointments: list[datetime]


class SFreeAppointments(BaseModel):
    specialization: str
    doctors: list[SFreeDoctorsAppointments]
