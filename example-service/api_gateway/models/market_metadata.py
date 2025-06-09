from pydantic import BaseModel
from datetime import datetime

class MarketMetadata(BaseModel):
    ticker: str
    name: str
    sector: str
    exchange: str
    