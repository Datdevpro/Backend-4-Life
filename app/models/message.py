from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.database.connection import Base

class MessageModel(Base):
    __tablename__ = "messages"

    "ID chính của message"
    id = Column(Integer, primary_key=True, index=True)

    "nội dung của message"
    content = Column(String, index=True)

    "conversation sở hữu message, dùng để biết message này thuộc về conversation nào"
    conversation_id = Column(Integer, ForeignKey("conversations.id"), nullable=False)

    # "user sở hữu message, dùng để biết message này thuộc về user nào"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # vai tro cua nguoi goi message, co the la "sender" hoac "receiver"
    role = Column(String, nullable=False)

    # Message content 
    content = Column(Text, nullable=False)
