from __future__ import annotations

from fastapi import APIRouter

from app.api.v1.photos import router as photos_router
from app.api.v1.todos import router as todos_router

api_router = APIRouter()
api_router.include_router(photos_router)
api_router.include_router(todos_router)
