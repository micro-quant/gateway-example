from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    env: str
    marketdata_csv_path: Optional[str] = None
    market_metadata_csv_path: Optional[str] = None
    db_url: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
