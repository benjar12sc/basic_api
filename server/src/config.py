import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# Get the absolute path to the data directory relative to this config file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "data", "sales.db"))
DATABASE_URL = f"sqlite+aiosqlite:///{DATA_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)

Base = declarative_base()