import re

from fastapi import APIRouter, Depends

from app.common.exceptions import UserDataIsNotValid
from app.models.users.users import Users
from app.services.users.dao import UsersDaO
from app.services.users.dependencies import get_current_user
from app.services.users.schemas import SUserPersonalData

router = APIRouter(prefix="/api/users", tags=["Данные пользователей"])


@router.post("/update_fullname")
async def update_user_full_name(pd: SUserPersonalData, user: Users = Depends(get_current_user)):
    name_pattern = re.compile(r'^[a-zA-Zа-яА-Я]*\Z')
    if ((
            pd.first_name is None or not re.search(name_pattern, pd.first_name)) and (
            pd.last_name is None or not re.search(name_pattern, pd.last_name)) and (
            pd.second_name is not None and not re.search(name_pattern, pd.second_name))):
        raise UserDataIsNotValid

    if user.pd_id is None:
        pd_id = await UsersDaO.add_full_name(pd)
        await UsersDaO.update_pd_id(user.id, pd_id)
    else:
        await UsersDaO.update_full_name(pd, user.pd_id)
