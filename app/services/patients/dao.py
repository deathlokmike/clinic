from app.services.dao.base import BaseDAO
from app.models.users.patients import Patients


class PatientsDAO(BaseDAO):
    model = Patients
