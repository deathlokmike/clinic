from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

if settings.MODE == "TEST":
    db_url = settings.TEST_DATABASE_URL
    db_params = {"poolclass": NullPool}
else:
    db_url = settings.DATABASE_URL
    db_params = {}

engine = create_async_engine(db_url, **db_params)

async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


class Base(AsyncAttrs, DeclarativeBase):
    pass
