from datetime import date

from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SExtendedUser(BaseModel):
    full_name: str
    birth_day: date
    gender: bool
    profile_photo_path: str


class SSensitiveSExtendedUser(SExtendedUser):
    passport_data: str
    address: str
    phone_number: str


class SPersonalData(BaseModel):
    first_name: str
    second_name: str
    last_name: str
    profile_photo_path: str

    @property
    def full_name(self) -> str:
        if self.second_name is None:
            return self.last_name + " " + self.first_name
        else:
            return self.last_name + " " + self.first_name + " " + self.second_name
