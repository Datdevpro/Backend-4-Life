from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth_dependency import get_current_user
from app.models.user import UserModel
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message_service import (
    create_user_message,
    get_messages_by_conversation
)


router = APIRouter(
    prefix="/conversations/{conversation_id}/messages",
    tags=["Messages"]
)


@router.post(
    "",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED
)
def add_message(
    conversation_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Tạo user message trong conversation hiện tại
    return create_user_message(
        conversation_id,
        message,
        db,
        current_user
    )


@router.get(
    "",
    response_model=list[MessageResponse]
)
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Lấy lịch sử message trong conversation hiện tại
    return get_messages_by_conversation(
        conversation_id,
        db,
        current_user
    )