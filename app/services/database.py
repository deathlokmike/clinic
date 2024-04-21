from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


if settings.MODE == "TEST":
    db_url = f"postgresql+asyncpg://{settings.get_test_database_url}"
    db_params = {"poolclass": NullPool}
else:
    db_url = f"postgresql+asyncpg://{settings.get_database_url}"
    db_params = {}

engine = create_async_engine(db_url, **db_params)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

if settings.MODE == "TEST":
    sync_db_url = f"postgresql+psycopg2://{settings.get_test_database_url}"
else:
    sync_db_url = f"postgresql+psycopg2://{settings.get_database_url}"

sync_engine = create_engine(sync_db_url)
sync_session = sessionmaker(sync_engine)
