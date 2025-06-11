from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables
load_dotenv()

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    future=True,
    class_=AsyncSession,
)

Base = declarative_base()