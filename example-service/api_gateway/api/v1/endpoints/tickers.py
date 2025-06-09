from fastapi import APIRouter, Depends
from api_gateway.datasources.base import DataSource
from api_gateway.dependencies import get_data_source

router = APIRouter()

# ********** /tickers - used for all ticker queries **********

@router.get("/tickers")
def list_symbols(data_source:DataSource=Depends(get_data_source)):
    return data_source.get_all_tickers()

@router.get("/tickers/metadata")
def get_symbol(data_source:DataSource=Depends(get_data_source)):
    return data_source.get_metadata()

# ********** /ticker - used for individual ticker queries **********

@router.get("/ticker/{ticker}/timeseries")
def get_symbol(ticker: str, data_source:DataSource=Depends(get_data_source)):
    return data_source.get_timeseries(ticker)