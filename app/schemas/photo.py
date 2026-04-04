from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic.config import ConfigDict


class PhotoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    original_filename: str
    content_type: str
    file_size: int
    created_at: datetime
