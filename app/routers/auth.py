from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database.session import get_db
from app.schemas.auth import UserRegister, UserResponse, UserLogin, Token
from app.services.auth_service import register_user, login_user
from app.dependencies.auth_dependency import get_current_user 
from app.models.user import UserModel


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)

def register(user: UserRegister, db: Session = Depends(get_db)):
    # Nhận email/password từ request body
    # Gọi service để hash password và lưu user vào database
    return register_user(user, db)
@router.post(
    "/login",
    response_model=Token
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # OAuth2PasswordRequestForm dùng field "username" và "password"
    # Trong project này, username được hiểu là email
    user = UserLogin(
        email=form_data.username,
        password=form_data.password
    )

    # Gọi service để kiểm tra email/password và tạo JWT token
    return login_user(user, db)


@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(current_user: UserModel = Depends(get_current_user)):
    # current_user được lấy từ JWT token thông qua dependency get_current_user
    # Nếu token hợp lệ, trả về thông tin user hiện tại 
    return current_user


