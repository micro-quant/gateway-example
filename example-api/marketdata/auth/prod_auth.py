# auth.py
import httpx
from fastapi import HTTPException
from jose import jwt
from jose.exceptions import JWTError
from typing import Dict
from functools import lru_cache

JWK_URL = "https://www.microquant.io/.well-known/jwks.json"
AUDIENCE = "microquant.io"

@lru_cache()
def get_jwk_keys():
    response = httpx.get(JWK_URL)
    response.raise_for_status()
    return response.json()["keys"]

def get_signing_key(kid: str) -> Dict:
    keys = get_jwk_keys()
    for key in keys:
        if key["kid"] == kid:
            return key
    raise HTTPException(status_code=401, detail="Invalid signing key")

async def verify_jwt(
    token: str,
) -> Dict:
    try:
        unverified_header = jwt.get_unverified_header(token)
        key = get_signing_key(unverified_header["kid"])
        payload = jwt.decode(
            token,
            key=key,
            algorithms=["RS256"],
            audience=AUDIENCE
        )
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token invalid: {str(e)}")
