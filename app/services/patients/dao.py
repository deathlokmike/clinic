from app.services.base_dao import BaseDAO
from app.models.users.patients import Patients


class PatientsDAO(BaseDAO):
    model = Patients
