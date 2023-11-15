from app.services.appointments.dao import AppointmentsDAO
from datetime import date
from fastapi import Depends
from app.services.users.dependencies import get_current_user
from app.models.users.users import Users


def get_free_intervals():
    pass


async def get_free_appointments(date: date, _: Users = Depends(get_current_user)):
    busy_appointments = await AppointmentsDAO.get_busy(date=date)
