import datetime
import json
import uuid

import pytest
from sqlalchemy import insert

from app.config import settings
from app.models.appointments import Appointments
from app.models.pneumonia import Pneumonia
from app.models.schedule import Schedule
from app.models.treatments import Treatments
from app.models.users.doctors import Doctors
from app.models.users.personal_data import PersonalData
from app.models.users.roles import Roles
from app.models.users.users import Users
from app.services.database import Base, async_session, engine


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
    personal_data = open_mock_json("personal_data")
    users = open_mock_json("users")
    doctors = open_mock_json("doctors")
    appointments = open_mock_json("appointments")
    schedule = open_mock_json("schedule")

    for u in users:
        u["id"] = uuid.UUID(u["id"])

    for p in personal_data:
        p["birth_day"] = datetime.datetime.strptime(p["birth_day"], "%Y-%m-%d")

    for d in doctors:
        d["date_employment"] = datetime.datetime.strptime(
            d["date_employment"], "%Y-%m-%d"
        )
        d["user_id"] = uuid.UUID(d["user_id"])

    for a in appointments:
        a["date_time"] = datetime.datetime.strptime(a["date_time"], "%Y-%m-%d %H:%M:%S")
        a["user_id"] = uuid.UUID(a["user_id"])

    for s in schedule:
        s["start_time"] = datetime.datetime.strptime(
            s["start_time"], "%Y-%m-%d %H:%M:%S"
        )
        s["end_time"] = datetime.datetime.strptime(
            s["end_time"], "%Y-%m-%d %H:%M:%S")

    async with async_session() as session:
        for Model, values in [
            (Roles, roles),
            (PersonalData, personal_data),
            (Users, users),
            (Doctors, doctors),
            (Appointments, appointments),
            (Schedule, schedule),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()
