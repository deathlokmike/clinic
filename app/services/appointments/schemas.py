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


class SNewAppointmentIn(BaseModel):
    doctor_id: int
    date_time: datetime

class SNewAppointmentOut(BaseModel):
    full_name: str
    date_time: datetime
    status: int