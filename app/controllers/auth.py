import datetime

from fastapi import APIRouter, Response

from app.common.exceptions import (IncorrectUserOrPassword,
                                   UserAlreadyExistsException)
from app.services.users.auth import (authenticate_user, create_access_token,
                                     get_password_hash)
from app.services.users.dao import UsersDaO
from app.services.users.schemas import SUserAuth

router = APIRouter(prefix="/api/auth", tags=["Авторизация и аутентификация"])


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDaO.get_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDaO.add(
        email=user_data.email,
        password=hashed_password,
        registration_date=datetime.datetime.utcnow(),
        role_id=0)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectUserOrPassword
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("clinic_access_token", access_token, httponly=True)


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("clinic_access_token")
