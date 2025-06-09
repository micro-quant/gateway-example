import os
import requests

from typing import List, Tuple

class _MarketDataClient:
    def __init__(self):
        market_data_url = os.getenv("MARKETDATA_URL")
        self.base_url = f'{market_data_url}/marketdata/api/v1'

    def _get(self, path: str):
        headers = {}
        token = os.getenv("AUTH_TOKEN_MICROQUANT")
        if token:
            headers['Authorization'] = f'Bearer {token}'
        response = requests.get(f'{self.base_url}{path}', timeout=5, headers=headers)
        response.raise_for_status()
        return response.json()

    def list_tickers(self) -> List[str]:
        data = self._get('/tickers')
        if not (isinstance(data, list) and all(isinstance(item, str) for item in data)):
            raise ValueError("Invalid API response format")
        return data
    
    def list_metadata(self) -> List[str]:
        data = self._get('/tickers/metadata')
        if not (isinstance(data, list) and all(isinstance(item, object) for item in data)):
            raise ValueError("Invalid API response format")
        return data

    def timeseries(self, ticker: str) -> List[Tuple[str, float]]:
        if not isinstance(ticker, str):
            raise ValueError("Ticker must be a string")
        data = self._get(f'/ticker/{ticker}/timeseries')
        if not (isinstance(data, list) and all(isinstance(item, list) and len(item) == 2 for item in data)):
            raise ValueError("Invalid API response format")
        return data

_client = None

def instance() -> _MarketDataClient:
    global _client
    if _client is None:
        _client = _MarketDataClient()
    return _client
