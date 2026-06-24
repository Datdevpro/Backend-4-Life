from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth_dependency import get_current_user
from app.models.user import UserModel
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse, TodoPatch
from app.services.todo_service import (
    get_all_todos,
    get_todo_by_id,
    create_todo,
    update_todo_by_id,
    delete_todo_by_id, 
    patch_todo_by_id
)


router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.get("", response_model=list[TodoResponse])
def get_todos(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Lấy danh sách todo của user hiện tại
    return get_all_todos(db, current_user)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Lấy một todo theo id, nhưng chỉ nếu todo đó thuộc user hiện tại
    return get_todo_by_id(todo_id, db, current_user)


@router.post(
    "",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
def add_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Tạo todo mới cho user hiện tại
    return create_todo(todo, db, current_user)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Update todo của user hiện tại
    return update_todo_by_id(todo_id, todo, db, current_user)


@router.patch("/{todo_id}", response_model=TodoResponse)
def patch_todo(
    todo_id: int,
    patch_data: TodoPatch,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Update một phần todo của user hiện tại
    return patch_todo_by_id(todo_id, patch_data, db, current_user)


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Xóa todo của user hiện tại
    delete_todo_by_id(todo_id, db, current_user)