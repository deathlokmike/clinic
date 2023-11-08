from app.services.dao.base import BaseDAO
from app.models.patients import Patients


class PatientsDAO(BaseDAO):
    model = Patients
