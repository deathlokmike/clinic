from fastapi import Depends
from app.services.users.dependencies import get_current_user
from app.services.patients.dao import PatientsDAO
from app.models.patients import Patients
from app.models.users import Users


async def get_current_patient(user: Users = Depends(get_current_user)) -> Patients:
    return await PatientsDAO.get_one_or_none(user_id=user.id)
