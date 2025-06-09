# add the stockviewer module to the Python path
import sys
import os

sys.path.append(os.path.abspath('./stockviewer'))

# Main code to demonstrate the shim functionality
import argparse
import os
import pandas as pd
from marketdata.tickers.list import handler as list_tickers
from marketdata.tickers.metadata import handler as ticker_metadata
from marketdata.tickers.timeseries import handler as ticker_timeseries

parser = argparse.ArgumentParser(description="Run in dev or prod mode")
parser.add_argument('--prod', action='store_true', help='Run in production mode')
args = parser.parse_args()

def main():
    # this is the shim; in microquant, this is set by the environment configuration and hence this entire file is not needed
    os.environ["MARKETDATA_URL"] = "http://localhost:8000"
    if args.prod:
        os.environ["AUTH_TOKEN_MICROQUANT"] = get_local_auth_token()
    else:
        os.environ["AUTH_TOKEN_MICROQUANT"] = gen_jwt()

    symbols = list_tickers()
    print("TICKERS:")
    [print(f'\t{symbol}') for symbol in symbols]

    df = ticker_metadata()
    print("\nTICKER METADATA:")
    print("\n".join(["\t" + line for line in repr(df).splitlines()]))

    ticker = "AAPL"
    timeseries = ticker_timeseries(ticker)
    print(f"\nTICKER TIMESERIES [{ticker}]:")
    print("\n".join(["\t" + line for line in repr(timeseries).splitlines()]))

def get_local_auth_token():
    # This function is used to get the local auth token for shim purposes
    # In production, this would be set by the environment configuration
    with open("./auth_token.txt", "r") as f:
        return f.read().strip()

def gen_jwt():
    import datetime
    from jose import jwt

    with open("../shared/private_key.pem", "r") as f:
        private_key = f.read()
        # This is a sample payload; similar to what microquant.io would generate
        payload = {
            "aud": "microquant.io",
            "email": "user@mail.com",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            "iat" : datetime.datetime.utcnow(),
            "iss": "https://microquant.io",
            "jti": "b5f899cf-d847-46b9-9c16-fa5de9b03557",
            "nbf": datetime.datetime.utcnow(),
            "sub": "BocIgnAAXBXDEFSAvDX9eLPRDlI3",
        }
        token = jwt.encode(payload, private_key, algorithm="RS256", headers={"kid": "1"})
        return token


if __name__ == "__main__":
    main()