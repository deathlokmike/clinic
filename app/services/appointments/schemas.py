from pydantic import BaseModel
from datetime import datetime


class SUserAppointment(BaseModel):
    date_time: datetime
    status: int
    specialization: str
    full_name: str
    profile_photo_path : str
