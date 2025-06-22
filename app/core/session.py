from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.settings import settings


engine = create_async_engine(
    settings.database_url,
    echo=False,
    pool_size=5,
    max_overflow=2,
    pool_recycle=3600,
    pool_pre_ping=True
)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()