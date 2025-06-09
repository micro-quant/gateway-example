import pandas as pd
from marketdata.client import marketdata_client

def handler() -> pd.DataFrame:
    metadata_list = marketdata_client.instance().list_metadata()
    return pd.DataFrame(metadata_list)
