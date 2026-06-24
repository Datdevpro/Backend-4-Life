from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # JWT secret key dùng để ký token
    SECRET_KEY: str

    # Thuật toán dùng cho JWT
    ALGORITHM: str = "HS256"

    # Thời gian token hết hạn, tính bằng phút
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database connection string
    DATABASE_URL: str

    # Cho Pydantic biết cần đọc biến môi trường từ file .env
    model_config = SettingsConfigDict(env_file=".env")


# Tạo object settings để import ở các file khác
settings = Settings()