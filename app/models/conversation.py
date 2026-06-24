from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base


class ConversationModel(Base):
    __tablename__ = "conversations"

    "ID chính của conversation"
    id = Column(Integer, primary_key=True, index=True)

    # "message của conversation"
    # message = Column(String, index=True)

    "tiêu đề của conversation"
    title = Column(String, index=True)

    "user sở hữu conversation, dùng để biết conversation này thuộc về user nào"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)