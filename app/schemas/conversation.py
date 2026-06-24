from pydantic import BaseModel

class ConversationCreate(BaseModel):
    title: str = "New conversation"

class ConversationResponse(BaseModel):
    id: int
    title: str
    user_id: int

    class Config:
        from_attributes = True