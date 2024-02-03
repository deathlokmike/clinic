from datetime import date

from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserPersonalData(BaseModel):
    first_name: str
    second_name: str | None
    last_name: str
    profile_photo_path: str = "img/default_profile_photo.png"

    @property
    def full_name(self) -> str:
        if self.second_name is None:
            return self.last_name + " " + self.first_name
        else:
            return self.last_name + " " + self.first_name + " " + self.second_name


class SExtendedUserData(SUserPersonalData):
    birth_day: date
    gender: bool


class SSensitiveSExtendedUserData(SExtendedUserData):
    passport_data: str
    address: str
    phone_number: str


class SUserInfo(BaseModel):
    id: str
    personal_data: SUserPersonalData
