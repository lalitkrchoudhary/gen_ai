from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class TodoBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    is_done: bool | None = None


class TodoRead(TodoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_done: bool
    created_at: datetime
    updated_at: datetime
