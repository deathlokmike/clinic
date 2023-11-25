from fastapi import APIRouter, Depends
from app.services.content.pneumonia.schemas import SPneumonia, SPneumoniaWithId
from app.services.content.pneumonia.dao import PneumoniaDAO
from app.models.users.users import Users
from app.services.users.dependencies import get_current_user

router = APIRouter(prefix="/api/pneumonia", tags=["Блок с пневмонией"])


@router.get("/all")
async def get_all_pneumonia_type() -> list[SPneumoniaWithId]:
    return await PneumoniaDAO.get_all()


@router.get("/{id}")
async def get_pneumonia_type(id_: int) -> SPneumoniaWithId | None:
    return await PneumoniaDAO.get_one_or_none(id=id_)


@router.post("", status_code=201)
async def add_pneumonia_type(
    pneumonia_data: SPneumonia, user: Users = Depends(get_current_user)
):
    await PneumoniaDAO.insert_value(
        type=pneumonia_data.type,
        pathogen=pneumonia_data.pathogen,
        morbidity=pneumonia_data.morbidity,
        mortality=pneumonia_data.mortality,
        severity=pneumonia_data.severity,
        symptoms=pneumonia_data.symptoms,
    )


@router.delete("/{id}", status_code=204)
async def delete_pneumonia_type(id_: int, user: Users = Depends(get_current_user)):
    await PneumoniaDAO.delete_value(id=id_)


@router.put("/{id}")
async def update_pneumonia_type(
    id_: int, pneumonia: SPneumonia, user: Users = Depends(get_current_user)
):
    await PneumoniaDAO.update_values(id_, pneumonia)
