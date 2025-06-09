import pandas as pd
from marketdata.client import marketdata_client

def handler(ticker: str) -> pd.DataFrame:
    timeseries_list = marketdata_client.instance().timeseries(ticker)

    # Extract datetime and value separately
    datetimes = pd.to_datetime([d[0] for d in timeseries_list])
    values = [d[1] for d in timeseries_list]

    # Create MultiIndex
    index = pd.MultiIndex.from_tuples(
        [(dt, ticker) for dt in datetimes],
        names=["timestamp", "id"]
    )

    return pd.Series(values, index=index)
