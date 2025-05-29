import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()  # Load from .env file

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    JWT_SECRET_KEY: str
    JWT_EXPIRATION_TIME: int = 3600
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
