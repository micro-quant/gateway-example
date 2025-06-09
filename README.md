# gateway-example

This repo contains two applications that demonstrate how a function in microquant can be used to access a secured API.

The two applications are `example-api` and `example-mqrepo`. The `example-api` is a FastAPI application that uses common auth middlewae to secure the API endpoints.  The `example-mqrepo` is an example repository that you might create and use inside microquant.  In this application, we use the `shim.py` file to run it locally, but this file is only for demonstration purposes and is not required in a production environment.

## Running the Application (dev-mode)

Ensure you have a virtual environment setup and the required dependencies installed (see the `Additional Information` section below for details).

```
# In a terminal, run the FastAPI application
cd examples-api
uvicorn marketdata.main:app --reload --env-file .env.dev --port 8000
```

```
# In a separate terminal, run the example application that fetches data from the FastAPI application
cd examples-mqrepo
python shim.py
```

## Running the Application (prod-mode)

Ensure you have a virtual environment setup and the required dependencies installed (see the `Additional Information` section below for details).

In order to correctly run in prod-mode, you must goto the file "examples-mqrepo/auth_token.txt" and replace the contents with a valid JWT that is generated directly in the microquant app.  This file contains further instructions on how to generate the JWT.

```
# In a terminal, run the FastAPI application
cd examples-api
uvicorn marketdata.main:app --reload --env-file .env.prod --port 8000
```

```
# In a separate terminal, run the example application that fetches data from the FastAPI application
cd examples-mqrepo
python shim.py --prod
```

## Additional Information

Setup your own virtual environment:
```
# create a virtual environment
python3 -m venv .venv
# activate the virtual environment
source .venv/bin/activate
# install the required dependencies
pip install -r requirements.txt
```

If you modify the dependencies, you should update the `requirements.txt` file to reflect those changes. This can be done by running the following commands:

```
# Add a new dependency
pip install <dependency-name>
# Update the requirements file
pip freeze > requirements.txt
```