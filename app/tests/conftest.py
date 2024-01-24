import datetime
import pytest
import json
from app.services.database import Base, async_session, engine
from app.models.users.roles import Roles
from app.models.users.users import Users
from app.models.users.doctors import Doctors
from app.models.users.patients import Patients
from app.models.users.personal_data import PersonalData
from app.models.pneumonia import Pneumonia
from app.models.appointments import Appointments
from app.models.treatments import Treatments
from app.models.schedule import Schedule
from app.config import settings
from sqlalchemy import insert
import uuid


@pytest.mark.asyncio
@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    roles = open_mock_json("roles")
    users = open_mock_json("users")
    personal_data = open_mock_json("personal_data")
    doctors = open_mock_json("doctors")
    patients = open_mock_json("patients")
    appointments = open_mock_json("appointments")
    schedule = open_mock_json("schedule")

    for u in users:
        u["id"] = uuid.UUID(u["id"])

    for p in personal_data:
        p["birth_day"] = datetime.datetime.strptime(p["birth_day"], "%Y-%m-%d")
        p["user_id"] = uuid.UUID(p["user_id"])

    for d in doctors:
        d["date_employment"] = datetime.datetime.strptime(
            d["date_employment"], "%Y-%m-%d"
        )

    for a in appointments:
        a["date_time"] = datetime.datetime.strptime(a["date_time"], "%Y-%m-%d %H:%M:%S")

    for s in schedule:
        s["start_time"] = datetime.datetime.strptime(
            s["start_time"], "%Y-%m-%d %H:%M:%S"
        )
        s["end_time"] = datetime.datetime.strptime(
            s["end_time"], "%Y-%m-%d %H:%M:%S")

    async with async_session() as session:
        for Model, values in [
            (Roles, roles),
            (Users, users),
            (PersonalData, personal_data),
            (Doctors, doctors),
            (Patients, patients),
            (Appointments, appointments),
            (Schedule, schedule),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()
