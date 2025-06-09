from api_gateway.dependencies import get_auth
from fastapi import FastAPI, Depends
from api_gateway.api.v1.endpoints import tickers

app = FastAPI(dependencies=[Depends(get_auth)])

app.include_router(tickers.router, prefix="/marketdata/api/v1")
