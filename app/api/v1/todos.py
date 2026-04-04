from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.crud.todo import create_todo, delete_todo, get_todo, list_todos, update_todo
from app.db.session import get_db
from app.schemas.todo import TodoCreate, TodoRead, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo_endpoint(payload: TodoCreate, db: Session = Depends(get_db)) -> TodoRead:
    return create_todo(db, payload)


@router.get("", response_model=list[TodoRead])
def list_todos_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[TodoRead]:
    return list_todos(db, skip=skip, limit=limit)


@router.get("/{todo_id}", response_model=TodoRead)
def get_todo_endpoint(todo_id: int, db: Session = Depends(get_db)) -> TodoRead:
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo_endpoint(todo_id: int, payload: TodoUpdate, db: Session = Depends(get_db)) -> TodoRead:
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return update_todo(db, todo, payload)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db)) -> Response:
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    delete_todo(db, todo)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
