from fastapi import HTTPException, status


class ClinicBaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(ClinicBaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class InsufficientRightsException(ClinicBaseException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "У вас недостаточно прав"


class IncorrectUserOrPassword(ClinicBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class TokenExpiredException(ClinicBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"


class TokenAbsentException(ClinicBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class UserIsNotPresentException(ClinicBaseException):
    status_code = status.HTTP_401_UNAUTHORIZED


class AppointmentNotAvailableException(ClinicBaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Запись к врачу недоступна"
