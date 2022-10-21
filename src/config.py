from pydantic import BaseSettings
import os

ENVIRONMENT_VARIABLE = "BLOG_ENV"
ENVIRONMENT = os.getenv(ENVIRONMENT_VARIABLE, "development")


class Settings(BaseSettings):
    """Environment variables declaration"""

    db_url: str
    debug: bool

    class Config:
        env_file = f".env.{ENVIRONMENT}"


settings = Settings()
