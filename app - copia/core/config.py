from pydantic import BaseModel
import os

class Settings(BaseModel):
    DB_NAME: str = "admin_tep"
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306

settings = Settings()

API_KEY = os.getenv("API_KEY", "dev_key_change_me")
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS",
    "http://localhost,http://localhost:5173,http://localhost:3000",
).split(",")
