from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str | None = None



class TodoUpdate(BaseModel):
    title: str
    description: str | None = None
    completed: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool

    # cho client biet toto nay thuoc ve user nao
    user_id : int 


    class Config:
         # Cho phép Pydantic đọc SQLAlchemy object
        from_attributes = True

class TodoPatch(BaseModel):
    # Các field đều optional vì PATCH chỉ update 1 phần data
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

    class Config:
        from_attributes = True