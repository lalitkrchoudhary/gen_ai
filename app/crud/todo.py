from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def create_todo(db: Session, data: TodoCreate) -> Todo:
    todo = Todo(title=data.title, description=data.description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo(db: Session, todo_id: int) -> Todo | None:
    return db.get(Todo, todo_id)


def list_todos(db: Session, *, skip: int = 0, limit: int = 100) -> list[Todo]:
    stmt = select(Todo).order_by(Todo.id).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def update_todo(db: Session, todo: Todo, data: TodoUpdate) -> Todo:
    patch = data.model_dump(exclude_unset=True)
    for key, value in patch.items():
        setattr(todo, key, value)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()
