from __future__ import annotations

from app import models  # noqa: F401
from app.db.base import Base
from app.db.session import engine


def init_db() -> None:
    # In production, prefer migrations (e.g. Alembic) over create_all.
    Base.metadata.create_all(bind=engine)
