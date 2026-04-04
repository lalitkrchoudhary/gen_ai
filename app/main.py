from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)
    yield


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
