from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.auth import UserRegister, UserLogin
from app.core.security import create_access_token


# Tạo công cụ hash password bằng bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    # Chuyển password thật thành password hash
    return pwd_context.hash(password)


def register_user(user: UserRegister, db: Session):
    # Kiểm tra email đã tồn tại chưa
    existing_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Tạo user mới với password đã hash
    new_user = UserModel(
        email=user.email,
        password_hash=hash_password(user.password)
    )

    # Lưu user vào database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def verify_password(plain_password: str, hashed_password: str):
    # So sánh password user nhập với password hash trong DB
    return pwd_context.verify(plain_password, hashed_password)

def login_user(user: UserLogin, db: Session):
    """
    Kiểm tra email/password.
    Nếu đúng, trả về JWT access token.
    """

    # Tìm user trong database bằng email
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()

    # Nếu email không tồn tại, trả lỗi 401
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Kiểm tra password user nhập có khớp password hash trong DB không
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Tạo JWT token, lưu email vào field "sub"
    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }