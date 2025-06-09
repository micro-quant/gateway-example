from marketdata.datasources.base import DataSource

class DbDataSource(DataSource):
    def __init__(self, db_connection: str):
        # TODO: Implement

    def get_all_tickers(self):
        # TODO: Implement
        return []

    def get_timeseries(self, ticker: str):
        # TODO: Implement
        return []

    def get_metadata(self, ticker: str):
        # TODO: Implement
        return []