import asyncio
import datetime
from datetime import date

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
from sqlalchemy.sql import text
import uuid


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    
    
    
    def get_raw() -> str:
        def last_day_of_month():
            next_month = date.today().replace(day=28) + datetime.timedelta(days=4)
            return next_month - datetime.timedelta(days=next_month.day)

        return text(
            f"""INSERT INTO schedule (start_time, end_time) SELECT date::timestamp + interval '8 hours' as start_time, date::timestamp + interval '17 hours' as end_time FROM generate_series('{date.today()}'::date, '{last_day_of_month()}'::date, '1 day') date WHERE EXTRACT(ISODOW FROM date) < 6"""
        )
        
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(get_raw())

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf8") as file:
            return json.load(file)

    roles = open_mock_json("roles")
    users = open_mock_json("users")
    personal_data = open_mock_json("personal_data")
    doctors = open_mock_json("doctors")
    patients = open_mock_json("patients")
    appointments = open_mock_json("appointments")

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

    async with async_session() as session:
        for Model, values in [
            (Roles, roles),
            (Users, users),
            (PersonalData, personal_data),
            (Doctors, doctors),
            (Patients, patients),
            (Appointments, appointments),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
