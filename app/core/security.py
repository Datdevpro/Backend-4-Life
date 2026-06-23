from datetime import datetime, timedelta, timezone

from jose import jwt


# Secret key dùng để ký JWT token
# Trong project thật, giá trị này phải đặt trong file .env, không hard-code
SECRET_KEY = "super-secret-key-change-this-later"

# Thuật toán dùng để ký token
ALGORITHM = "HS256"

# Thời gian token hết hạn, tính bằng phút
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Gắn thời gian hết hạn vào payload
    to_encode.update({"exp": expire})

    # Encode payload thành JWT token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt