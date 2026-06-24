from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.conversation import ConversationModel
from app.models.user import UserModel
from app.schemas.conversation import ConversationCreate


def create_conversation(
    conversation: ConversationCreate,
    db: Session,
    current_user: UserModel
):
    # Tạo conversation mới và gắn với user hiện tại
    new_conversation = ConversationModel(
        title=conversation.title,
        user_id=current_user.id
    )

    # Lưu conversation vào database
    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return new_conversation


def get_all_conversations(
    db: Session,
    current_user: UserModel
):
    # Chỉ lấy conversation thuộc về user hiện tại
    return (
        db.query(ConversationModel)
        .filter(ConversationModel.user_id == current_user.id)
        .all()
    )


def get_conversation_by_id(
    conversation_id: int,
    db: Session,
    current_user: UserModel
):
    # Tìm conversation theo id và đảm bảo nó thuộc về user hiện tại
    conversation = (
        db.query(ConversationModel)
        .filter(
            ConversationModel.id == conversation_id,
            ConversationModel.user_id == current_user.id
        )
        .first()
    )

    # Nếu không tồn tại hoặc thuộc user khác thì trả 404
    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return conversation