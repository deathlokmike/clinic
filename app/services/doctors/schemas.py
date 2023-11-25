import datetime
from pydantic import BaseModel
from app.services.appointments.schemas import SBookedAppointment
from app.services.users.schemas import SPersonalData


class SDoctorWithAppointment(BaseModel):
    id: int
    specialization: str
    date_employment: datetime.date
    pre_work_experience: int
    personal_data: SPersonalData
    appointments: list[SBookedAppointment]

    @property
    def experience(self) -> int:
        return (
            datetime.date.today() - self.date_employment
        ).days // 365 + self.pre_work_experience


class SAppointmentsByDate(BaseModel):
    date: datetime.date
    time: list[datetime.time]


class SDoctorWithFreeAppointments(BaseModel):
    id: int
    full_name: str
    experience: int
    profile_photo_path: str
    free_appointments: list[SAppointmentsByDate]


class SAvailableAppointments(BaseModel):
    specialization: str
    doctors: list[SDoctorWithFreeAppointments]
