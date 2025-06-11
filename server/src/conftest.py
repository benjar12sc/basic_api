import os
import pytest
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config import Base
from dotenv import load_dotenv

# Load test environment
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env_test'))

test_db_url = os.getenv("DATABASE_URL")
engine = create_async_engine(test_db_url, echo=True, future=True)
TestSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    future=True,
    class_="AsyncSession",
)

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_db():
    # Create tables
    import asyncio
    async def create_all():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    asyncio.run(create_all())
    yield
    # Drop tables and remove test db
    async def drop_all():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    asyncio.run(drop_all())
    db_path = test_db_url.replace("sqlite+aiosqlite:///", "")
    if os.path.exists(db_path):
        os.remove(db_path)
