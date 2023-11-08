from pydantic import BaseModel
from datetime import datetime
from app.services.patients.schemas import SExtendedUser


class SUserAppointment(BaseModel):
    date_time: datetime
    status: int
    specialization: str
    full_name: str
    profile_photo_path : str


class SAppointmentsWithPatientInfo(BaseModel):
    patient: SExtendedUser
    appointments: list[SUserAppointment]
