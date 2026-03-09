from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.testing import future

DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/institute_db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True, #set to tue if you want tot see sql statements produced by admin

    pool_pre_ping = True ,#verify the connection in pool before using them
    future=True
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit =False
)

async def get_db() -> AsyncGenerator[AsyncSession,None]:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()