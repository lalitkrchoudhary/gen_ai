from __future__ import annotations

import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.photo import Photo


def _build_storage_path(filename: str | None) -> tuple[str, Path]:
    safe_name = Path(filename or "upload").name
    suffix = Path(safe_name).suffix.lower()
    stored_filename = f"{uuid4().hex}{suffix}"
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)
    return safe_name, upload_dir / stored_filename


def create_photo(db: Session, upload: UploadFile) -> Photo:
    content_type = (upload.content_type or "").lower()
    if not content_type.startswith("image/"):
        raise ValueError("Only image uploads are supported")

    original_filename, file_path = _build_storage_path(upload.filename)

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(upload.file, buffer)

        photo = Photo(
            original_filename=original_filename,
            stored_filename=file_path.name,
            content_type=content_type,
            file_path=str(file_path),
            file_size=file_path.stat().st_size,
        )
        db.add(photo)
        db.commit()
        db.refresh(photo)
        return photo
    except Exception:
        db.rollback()
        if file_path.exists():
            file_path.unlink()
        raise
    finally:
        upload.file.close()


def get_photo(db: Session, photo_id: int) -> Photo | None:
    return db.get(Photo, photo_id)


def list_photos(db: Session, *, skip: int = 0, limit: int = 100) -> list[Photo]:
    stmt = select(Photo).order_by(Photo.id).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())
