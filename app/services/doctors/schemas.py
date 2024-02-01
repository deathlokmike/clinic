import datetime

from pydantic import BaseModel

from app.services.users.schemas import SUserInfo, SUserPersonalData


class SDoctorWithPersonalData(BaseModel):
    id: int
    specialization: str
    user: SUserInfo


class SBookedAppointment(BaseModel):
    date_time: datetime.datetime


class SDoctorWithBookedAppointments(SDoctorWithPersonalData):
    date_employment: datetime.date
    pre_work_experience: int
    appointments: list[SBookedAppointment]

    @property
    def experience(self) -> int:
        return (datetime.date.today() - self.date_employment).days // 365 + self.pre_work_experience


class SFreeAppointmentsTimeGroupedByDate(BaseModel):
    date: datetime.date
    time: list[datetime.time]


class SDoctorWithFreeAppointments(BaseModel):
    id: int
    experience: int
    personal_data: SUserPersonalData
    free_appointments: list[SFreeAppointmentsTimeGroupedByDate]


class SAvailableAppointments(BaseModel):
    specialization: str
    doctors: list[SDoctorWithFreeAppointments]
