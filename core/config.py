from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    HOST: str
    PORT: int
    DEBUG: bool
    RELOAD: bool

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    ASYNC_DATABASE_URL: str
    SYNC_DATABASE_URL: str

    REFRESH_TOKEN_EXPIRE_MINUTES: int
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_SECRET_KEY: str
    ALGORITHM: str
    TOKEN_KEY: str



    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()