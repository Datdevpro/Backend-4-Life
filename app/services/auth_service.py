from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.auth import UserRegister


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