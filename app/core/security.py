from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from app.core.config import settings


# Secret key dùng để ký JWT token
# Trong project thật, giá trị này phải đặt trong file .env, không hard-code



def create_access_token(data: dict):
    """
    Tạo JWT access token.

    data thường chứa thông tin định danh user,
    ví dụ: {"sub": "lee@example.com"}
    """

    # Copy data để tránh sửa trực tiếp object gốc
    to_encode = data.copy()

    # Tạo thời điểm hết hạn token
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Gắn thời gian hết hạn vào payload
    to_encode.update({"exp": expire})

    # Encode payload thành JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


def decode_access_token(token: str ):
    """
    Giải mã JWT access token.

    Nếu token hợp lệ, trả về payload (dict).
    Nếu token không hợp lệ, raise exception.
    """
    try: 
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload
    except JWTError:
        return None
