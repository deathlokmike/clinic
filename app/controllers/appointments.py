from fastapi import APIRouter, Depends
from pydantic import TypeAdapter

from app.models.users.users import Users
from app.services.appointments.dao import AppointmentsDAO
from app.services.appointments.dependecies.book import book_new_appointment
from app.services.appointments.dependecies.get_free import \
    get_free_appointments
from app.services.appointments.schemas import (SNewAppointmentIn,
                                               SNewAppointmentOut,
                                               SPatientInfoWithAppointments)
from app.services.doctors.schemas import SAvailableAppointments
from app.services.users.dependencies import get_current_user

router = APIRouter(prefix="/api/appointments", tags=["Записи на прием"])


@router.get("")
async def get_patient_info_and_appointments(
        user: Users = Depends(get_current_user)) -> SPatientInfoWithAppointments | None:
    if user.pd_id is None:
        return None
    raw = await AppointmentsDAO.get_patient_appointments(user.id)
    return TypeAdapter(SPatientInfoWithAppointments).validate_python(raw["Users"])


@router.get("/available")
async def get_available_appointments(
        available_appointments: list[SAvailableAppointments] = Depends(get_free_appointments)
) -> list[SAvailableAppointments]:
    return available_appointments


@router.post("/book")
async def book_appointment(
        new_appointment: SNewAppointmentIn, user: Users = Depends(get_current_user)) -> SNewAppointmentOut:
    result: SNewAppointmentOut = await book_new_appointment(user.id, new_appointment)
    return result
