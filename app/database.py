import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

os.makedirs("/app/data", exist_ok=True)

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:////app/data/tasks.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session() as session:
        yield session