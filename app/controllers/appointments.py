from fastapi import APIRouter, Depends
from app.models.users import Users
from app.services.users.dependencies import get_current_user
from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.schemas import SUserAppointment


router = APIRouter(
    prefix="/api/appointments",
    tags=["Записи на прием"]
)


@router.get("")
async def get_patient_appointments(user: Users = Depends(get_current_user)) -> list[SUserAppointment]:
    appointments = await AppointmentsDAO.get_patient_appointments(user_id=user.id)
    return appointments
