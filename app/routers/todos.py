from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.services.todo_service import (
    get_all_todos,
    get_todo_by_id,
    create_todo,
    update_todo_by_id,
    delete_todo_by_id
)

#### còn đây là file tạo các endpoint, các route liên quan đến TodoModel. ####

router = APIRouter()


@router.get("/todos", response_model=list[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return get_all_todos(db)


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    return get_todo_by_id(todo_id, db)


@router.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def add_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(todo, db)


@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo_by_id(todo_id, todo, db)


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo_by_id(todo_id, db)