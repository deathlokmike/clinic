from fastapi import APIRouter, Depends
from app.models.users.personal_data import PersonalData
from app.services.users.dependencies import get_personal_data
from app.services.appointments.dao import AppointmentsDAO
from app.services.patients.dao import PatientsDAO
from app.services.users.schemas import SExtendedUser
from app.services.appointments.schemas import SAppointmentsWithPatientInfo
from app.services.appointments.dependencies import get_free_appointments
from app.services.doctors.schemas import SAvailableAppointments
from pydantic import TypeAdapter


router = APIRouter(prefix="/api/appointments", tags=["Записи на прием"])


@router.get("")
async def get_patient_info_and_appointments(
    pd: PersonalData = Depends(get_personal_data),
) -> SAppointmentsWithPatientInfo:
    patient = await PatientsDAO.get_one_or_none(pd_id=pd.id)
    appointments = await AppointmentsDAO.get_patient_appointments(patient_id=patient.id)
    personal_data = TypeAdapter(SExtendedUser).validate_python(pd).model_dump()
    return {"personal_data": personal_data, "appointments": appointments}


@router.get("/available")
async def get_available_appointments(
    available_appointments: list[SAvailableAppointments] = Depends(
        get_free_appointments
    ),
) -> list[SAvailableAppointments]:
    return available_appointments
