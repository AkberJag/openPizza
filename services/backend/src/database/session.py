from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from src.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    """Create a new database session and close it when the request is complete"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
