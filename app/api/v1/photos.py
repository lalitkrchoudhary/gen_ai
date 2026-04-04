from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.crud.photo import create_photo, get_photo, list_photos
from app.db.session import get_db
from app.schemas.photo import PhotoRead

router = APIRouter(prefix="/photos", tags=["photos"])


@router.post("/upload", response_model=PhotoRead, status_code=status.HTTP_201_CREATED)
def upload_photo_endpoint(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> PhotoRead:
    try:
        return create_photo(db, file)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("", response_model=list[PhotoRead])
def list_photos_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[PhotoRead]:
    return list_photos(db, skip=skip, limit=limit)


@router.get("/{photo_id}", response_model=PhotoRead)
def get_photo_endpoint(photo_id: int, db: Session = Depends(get_db)) -> PhotoRead:
    photo = get_photo(db, photo_id)
    if photo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")
    return photo


@router.get("/{photo_id}/download")
def download_photo_endpoint(photo_id: int, db: Session = Depends(get_db)) -> FileResponse:
    photo = get_photo(db, photo_id)
    if photo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")

    file_path = Path(photo.file_path)
    if not file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo file not found")

    return FileResponse(
        path=file_path,
        media_type=photo.content_type,
        filename=photo.original_filename,
    )
