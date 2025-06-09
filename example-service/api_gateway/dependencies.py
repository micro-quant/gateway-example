from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from api_gateway.core.config import settings
from api_gateway.datasources.base import DataSource

def get_data_source() -> DataSource:
    if settings.env == "prod":
        # from api_gateway.datasources.db import DbDataSource
        # return DbDataSource(db_connection=settings.db_url)
        from api_gateway.datasources.csv import CsvDataSource
        return CsvDataSource(marketdata_path=settings.marketdata_csv_path, market_metadata_path=settings.market_metadata_csv_path)
    else:
        from api_gateway.datasources.csv import CsvDataSource
        return CsvDataSource(marketdata_path=settings.marketdata_csv_path, market_metadata_path=settings.market_metadata_csv_path)

bearer_scheme = HTTPBearer()

async def get_auth(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    if settings.env == "prod":
        from api_gateway.auth.prod_auth import verify_jwt
        return await verify_jwt(token)
    else:
        from api_gateway.auth.dev_auth import verify_jwt
        return await verify_jwt(token)