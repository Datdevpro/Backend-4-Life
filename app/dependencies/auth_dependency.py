from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.user import UserModel


# oauth2_scheme sẽ đọc token từ header:
# Authorization: Bearer <token>
bearer_scheme = HTTPBearer(bearerFormat="JWT")


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    """
    Dependency dùng để lấy user hiện tại từ JWT token.

    Flow:
    1. Lấy token từ Authorization header
    2. Decode token
    3. Lấy email từ payload["sub"]
    4. Tìm user trong database
    5. Return user
    """

    # Decode token để lấy payload
    token = credentials.credentials
    payload = decode_access_token(token)

    # Nếu token sai hoặc hết hạn
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    # Lấy email từ field "sub"
    email = payload.get("sub")

    # Nếu token không có email
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )

    # Tìm user trong database bằng email
    user = db.query(UserModel).filter(UserModel.email == email).first()

    # Nếu user không còn tồn tại
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user
