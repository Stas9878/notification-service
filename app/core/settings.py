from functools import cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # RabbitMQ
    RMQ_USER: str
    RMQ_PASS: str
    RMQ_HOST: str
    RMQ_PORT: int
    RMQ_QUEUE: str

    # Email
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    class Config:
        env_file = '.env'


@cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()