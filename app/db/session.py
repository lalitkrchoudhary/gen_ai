from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings


connect_args = {}
if settings.database_url.startswith("sqlite"):
    # needed for SQLite when using a single file across threads
    connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.database_url,
    echo=settings.sqlalchemy_echo,
    connect_args=connect_args,
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=Session)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
