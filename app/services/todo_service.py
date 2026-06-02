from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.todo import TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate

#### Đây là file tạo các xử lý logic, các hàm xử lý dữ liệu,
# tương tác với database,... liên quan đến TodoModel. ####

def get_all_todos(db: Session):
    return db.query(TodoModel).all()


def get_todo_by_id(todo_id: int, db: Session):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


def create_todo(todo: TodoCreate, db: Session):
    new_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=False
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


def update_todo_by_id(todo_id: int, updated_todo: TodoUpdate, db: Session):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo_by_id(todo_id: int, db: Session):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted",
        "deleted_id": todo_id
    }