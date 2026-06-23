from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import UserRegister, UserResponse, UserLogin, Token
from app.services.auth_service import register_user, login_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)

@router.post(
    "/login",
    response_model=Token
)
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Nhận email/password từ request body
    # Gọi service để kiểm tra login và tạo JWT token
    return login_user(user, db)


def register(user: UserRegister, db: Session = Depends(get_db)):
    # Nhận email/password từ request body
    # Gọi service để hash password và lưu user vào database
    return register_user(user, db)