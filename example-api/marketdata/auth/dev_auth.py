# auth.py
import httpx
from fastapi import HTTPException
from jose import jwt
from jose.exceptions import JWTError
from typing import Dict

AUDIENCE = "microquant.io"

def get_public_key() -> str:
    with open("../shared/public_key.pem", "r") as f:
        public_key = f.read()
        return public_key

async def verify_jwt(
    token: str,
) -> Dict:
    try:
        unverified_header = jwt.get_unverified_header(token)
        key = get_public_key()
        payload = jwt.decode(
            token,
            key=key,
            algorithms=["RS256"],
            audience=AUDIENCE
        )
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token invalid: {str(e)}")
