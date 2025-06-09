from abc import ABC, abstractmethod
from typing import List, Tuple
from api_gateway.models.market_metadata import MarketMetadata

class DataSource(ABC):
    @abstractmethod
    def get_all_tickers(self) -> List[str]:
        pass

    @abstractmethod
    def get_timeseries(self, ticker: str) -> List[Tuple[str, float]]:
        pass

    @abstractmethod
    def get_metadata(self) -> List[MarketMetadata]:
        pass
