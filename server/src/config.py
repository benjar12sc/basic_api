from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# TODO: Move this to .env file
DATABASE_URL = "sqlite+aiosqlite:///../data/sales.db"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)

Base = declarative_base()