from datetime import datetime, timedelta
from pydantic import EmailStr
from passlib.context import CryptContext
from jose import jwt

from app.config import settings
from app.services.users.dao import UsersDaO
from app.models.users import Users


_pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return _pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return _pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, settings.JWT_ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str) -> Users | None:
    user = await UsersDaO.get_one_or_none(email=email)
    if user and verify_password(password, user.password):
        return user
    return None
