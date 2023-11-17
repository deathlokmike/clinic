from pydantic import BaseModel
from datetime import datetime
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
    patient_id: int | None
    date_time: datetime | None
