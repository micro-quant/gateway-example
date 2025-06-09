# gateway-example

This repo demonstrates how to access a secured API via microquant.

This repo demonstrates secure API access via 2 applications, these applications are `example-service` and `example-client`. The `example-service` is a FastAPI application that uses common auth middleware to secure the API endpoints.  The `example-client` is an example application that you might create and use inside microquant.  In this application, we use the `dev_cli.py` file to run it locally, but this file is only for demonstration purposes and is not required in a production environment.

## Running the Application (dev-mode)

Ensure you have a virtual environment setup and the required dependencies installed for each terminal you open (see the `Additional Information` section below for details).

```
# In a terminal, run the FastAPI application
cd example-service
uvicorn api_gateway.main:app --reload --env-file .env.dev --port 8000
```

```
# In a separate terminal, run the example application that fetches data from the FastAPI application
cd example-client
python dev_cli.py
```

## Running the Application (prod-mode)

Ensure you have a virtual environment setup and the required dependencies installed (see the `Additional Information` section below for details).

In order to correctly run in prod-mode, you must goto the file "example-client/auth_token.txt" and replace the contents with a valid JWT that is generated directly in the microquant app.  This file contains further instructions on how to generate the JWT.

```
# In a terminal, run the FastAPI application
cd example-service
uvicorn api_gateway.main:app --reload --env-file .env.prod --port 8000
```

```
# In a separate terminal, run the example application that fetches data from the FastAPI application
cd example-client
python dev_cli.py --prod
```

## Key Areas of Interest

Below are some key topics  used in external api's that you might call from within microquant:

- To verify these headers with microquant's JWK public keys, see [`prod_auth.py`](https://github.com/micro-quant/gateway-example/blob/main/example-service/api_gateway/auth/prod_auth.py)

Below are some key topics used within microquant applications:

- To retrieve and propogate auth headers to external services, see [`marketdata_client.py#L13`](https://github.com/micro-quant/gateway-example/blob/main/example-client/marketdata/client/marketdata_client.py#L13)
- To see a good practice of how to abstract the API calls with a single client via a singleton, see [`marketdata_client.py#L42`](https://github.com/micro-quant/gateway-example/blob/main/example-client/marketdata/client/marketdata_client.py#L42)

## Additional Information

First, make sure you clone this repository locally.  Then, to setup your own virtual environment, this needs to be done once per application (ie once in example-client and once in example-service).

```
# change directories into either example-service or example-client
cd example-service  # or cd example-client
# create a virtual environment
python3 -m venv .venv
# activate the virtual environment
source .venv/bin/activate
# install the required dependencies
pip install -r requirements.txt
```

If you modify the dependencies, you should update the `requirements.txt` file to reflect those changes. This can be done by running the following commands:

```
# change directories into either example-service or example-client
cd example-service  # or cd example-client
# Add a new dependency
pip install <dependency-name>
# Update the requirements file
pip freeze > requirements.txt
```
