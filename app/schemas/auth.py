from pydantic import BaseModel


class UserRegister(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    # Email dùng để login
    email: str

    # Password user nhập khi login
    password: str


class Token(BaseModel):
    # JWT token server trả về
    access_token: str

    # Loại token
    token_type: str