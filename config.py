# config.py - Environment Configuration (No MongoDB)
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama3-70b-8192"
    APP_ENV: str = "development"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
