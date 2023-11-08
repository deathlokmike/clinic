from pydantic import BaseModel
from datetime import date


class SExtendedUser(BaseModel):
    full_name: str
    birth_day: date
    gender: bool
    profile_photo_path: str


class SSensitiveSExtendedUser(SExtendedUser):
    passport_data: str
    address: str
    phone_number: str
