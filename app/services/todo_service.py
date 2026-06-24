from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.todo import TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate, TodoPatch
from app.models.user import UserModel

#### Đây là file tạo các xử lý logic, các hàm xử lý dữ liệu,
# tương tác với database,... liên quan đến TodoModel. ####

def get_all_todos(db: Session, current_user: UserModel):
    # Chỉ lấy các todo thuộc về user hiện tại
    return (
        db.query(TodoModel)
        .filter(TodoModel.user_id == current_user.id)
        .all()
    )


def get_todo_by_id(todo_id: int, db: Session, current_user: UserModel):
    todo = ( db.query(TodoModel)
            .filter(
        TodoModel.id == todo_id, 
        TodoModel.user_id == current_user.id 
    )
    .first()
    )

    # If khong thay, return 404

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


def create_todo(todo: TodoCreate, db: Session, current_user: UserModel):
    new_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=False, 
        user_id = current_user.id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


def update_todo_by_id(todo_id: int, updated_todo: TodoUpdate, db: Session, current_user: UserModel):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == current_user.id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo_by_id(todo_id: int, db: Session, current_user: UserModel):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == current_user.id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted",
        "deleted_id": todo_id
    }

def patch_todo_by_id(todo_id: int, patch_data: TodoPatch, db: Session, current_user: UserModel):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == current_user.id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

     # Chuyển Pydantic object thành dict
    # exclude_unset=True nghĩa là chỉ lấy các field client thật sự gửi lên``
    # Cập nhật các field được gửi trong request
    updated_fields = patch_data.model_dump(exclude_unset=True)
    for field, value in updated_fields.items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)

    return todo