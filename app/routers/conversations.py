from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth_dependency import get_current_user
from app.models.user import UserModel
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse
)
from app.services.conversation_service import (
    create_conversation,
    get_all_conversations,
    get_conversation_by_id
)


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post(
    "",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED
)
def add_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Tạo conversation mới cho user hiện tại
    return create_conversation(conversation, db, current_user)


@router.get(
    "",
    response_model=list[ConversationResponse]
)
def get_conversations(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Lấy tất cả conversations của user hiện tại
    return get_all_conversations(db, current_user)


@router.get(
    "/{conversation_id}",
    response_model=ConversationResponse
)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Lấy một conversation theo id, nhưng chỉ nếu thuộc về user hiện tại
    return get_conversation_by_id(conversation_id, db, current_user)