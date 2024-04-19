import sys

from sqlalchemy import text

sys.path.append("/clinic")

from app.services.database import sync_session
from app.tasks.scheduled import set_actual_schedule

set_actual_schedule()

with sync_session() as session:
    query = text("SELECT * FROM roles")
    result = session.execute(query)
    if len(result.scalars().all()) == 0:
        with open("./setup/init.sql") as file:
            query = text(file.read())
            session.execute(query)
            session.commit()
