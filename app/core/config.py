from typing import Optional

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    MONGO_DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
