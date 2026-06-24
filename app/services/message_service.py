from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.conversation import ConversationModel
from app.models.message import MessageModel
from app.models.user import UserModel
from app.schemas.message import MessageCreate


def get_conversation_or_404(
    conversation_id: int,
    db: Session,
    current_user: UserModel
):
    # Kiểm tra conversation có tồn tại và thuộc về user hiện tại không
    conversation = (
        db.query(ConversationModel)
        .filter(
            ConversationModel.id == conversation_id,
            ConversationModel.user_id == current_user.id
        )
        .first()
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return conversation


def create_user_message(
    conversation_id: int,
    message: MessageCreate,
    db: Session,
    current_user: UserModel
):
    # Đảm bảo user chỉ gửi message vào conversation của chính họ
    get_conversation_or_404(conversation_id, db, current_user)

    # 1. Lưu message do user gửi
    user_message = MessageModel(
        conversation_id=conversation_id,
        user_id=current_user.id,
        role="user",
        content=message.content
    )

    db.add(user_message)
    db.commit()
    db.refresh(user_message)

    # 2. Tạo assistant response giả lập
    # Sau này đoạn này sẽ được thay bằng OpenAI / Gemini / Claude API
    assistant_message = MessageModel(
        conversation_id=conversation_id,
        user_id=current_user.id,
        role="assistant",
        content=f"Mock assistant response to: {message.content}"
    )

    db.add(assistant_message)
    db.commit()
    db.refresh(assistant_message)

    # 3. Trả về message của assistant cho client
    return assistant_message


def get_messages_by_conversation(
    conversation_id: int,
    db: Session,
    current_user: UserModel
):
    # Đảm bảo conversation thuộc về user hiện tại
    get_conversation_or_404(conversation_id, db, current_user)

    # Lấy toàn bộ messages trong conversation đó
    return (
        db.query(MessageModel)
        .filter(
            MessageModel.conversation_id == conversation_id,
            MessageModel.user_id == current_user.id
        )
        .order_by(MessageModel.id.asc())
        .all()
    )