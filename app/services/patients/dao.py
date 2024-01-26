from app.models.users.patients import Patients
from app.services.base_dao import BaseDAO


class PatientsDAO(BaseDAO):
    model = Patients
