from marketdata.client import marketdata_client
from typing import List

def handler() -> List[str]:
    return marketdata_client.instance().list_tickers()
