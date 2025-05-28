import os
from dotenv import load_dotenv

env_file = f".env.{os.getenv('ENV', 'development')}"
load_dotenv(dotenv_path=env_file)

class Settings:
    ENV = os.getenv("ENV")
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()