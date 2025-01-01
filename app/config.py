from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "")

settings = Settings()
