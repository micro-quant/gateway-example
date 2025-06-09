import csv
from pathlib import Path
from api_gateway.datasources.base import DataSource
from api_gateway.models.market_data_point import MarketDataPoint
from api_gateway.models.market_metadata import MarketMetadata

class CsvDataSource(DataSource):
    def __init__(self, marketdata_path: str, market_metadata_path: str):
        self.datapoints = load_marketdata(marketdata_path)
        self.metadata = load_marketmetadata(market_metadata_path)

    def get_all_tickers(self):
        return list(dict.fromkeys([point.ticker for point in self.datapoints]))

    def get_timeseries(self, ticker: str):
        return [(point.datetime, point.value) for point in self.datapoints if point.ticker == ticker and point.property == "intraday_price"]

    def get_metadata(self):
        return self.metadata

def load_marketdata(path: str) -> list[MarketDataPoint]:
    points = []
    csv_path = Path(path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at {csv_path}")

    with csv_path.open(mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["value"] = float(row["value"])
                point = MarketDataPoint(**row)
                points.append(point)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e}")
    
    return points

def load_marketmetadata(path: str) -> list[MarketMetadata]:
    mdlist = []
    csv_path = Path(path)

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found at {csv_path}")

    with csv_path.open(mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                md = MarketMetadata(**row)
                mdlist.append(md)
            except (ValueError, KeyError) as e:
                print(f"Skipping row due to error: {e}")
    
    return mdlist
