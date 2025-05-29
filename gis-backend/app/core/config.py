import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()  # Load from .env file

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
