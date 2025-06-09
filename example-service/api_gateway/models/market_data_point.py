from pydantic import BaseModel
from datetime import datetime

class MarketDataPoint(BaseModel):
    ticker: str
    property: str
    datetime: datetime
    value: float
    