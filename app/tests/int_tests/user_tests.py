import pytest
from pydantic import TypeAdapter

from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.schemas import SPatientInfoWithAppointments
from app.services.users.dao import UsersDaO


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_id, count_appointments",
    [
        ("982eeb52-667c-4acb-9d83-18d7d48f518a", 4),
        ("95291318-f3fa-4f0f-b3a0-8908bfe391b6", 2),
        ("2a4e3522-f10f-4fdf-a714-3e58f451c92e", 1),
        ("5632918c-135b-4c49-8af5-89ed75158fb1", 0)
    ],
)
async def test_user_appointment_by_depends(user_id: str, count_appointments: int):
    user = await UsersDaO.get_by_id(user_id)
    raw = await AppointmentsDAO.get_patient_appointments(user.id)
    user_with_appointments: SPatientInfoWithAppointments = (
        TypeAdapter(SPatientInfoWithAppointments).validate_python(raw["Users"]))
    assert len(user_with_appointments.appointments) == count_appointments
