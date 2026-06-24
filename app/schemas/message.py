from pydantic import BaseModel


class MessageCreate(BaseModel):
    # Nội dung user gửi vào conversation
    content: str


class MessageResponse(BaseModel):
    # Data message trả về cho client
    id: int
    conversation_id: int
    user_id: int
    role: str
    content: str

    class Config:
        # Cho phép Pydantic đọc SQLAlchemy object
        from_attributes = True