from fastapi import APIRouter, Depends
from app.models.patients import Patients
from app.services.patients.dependencies import get_current_patient
from app.services.appointments.dao import AppointmentsDAO
from app.services.doctors.dao import DoctorsDAO
from app.services.patients.schemas import SExtendedUser
from app.services.appointments.schemas import SAppointmentsWithPatientInfo
from pydantic import TypeAdapter
from datetime import date


router = APIRouter(prefix="/api/appointments", tags=["Записи на прием"])


@router.get("")
async def get_patient_info_and_appointments(
    patient: Patients = Depends(get_current_patient),
) -> SAppointmentsWithPatientInfo:
    appointments = await AppointmentsDAO.get_patient_appointments(patient_id=patient.id)
    patient = TypeAdapter(SExtendedUser).validate_python(patient).model_dump()
    return {"patient": patient, "appointments": appointments}


@router.get("/free")
async def get_free_appointments(date: date):
    busy_appointments = await DoctorsDAO.get_busy(date)
