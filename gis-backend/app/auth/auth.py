import os
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
JWKS_URL = f"{SUPABASE_URL}/auth/v1/keys"
security = HTTPBearer()

# Fetch and cache the JSON Web Key Set
def get_jwks():
    response = requests.get(JWKS_URL)
    if response.status_code != 200:
        raise Exception("Failed to fetch JWKS")
    return response.json()["keys"]

JWKS = get_jwks()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = credentials.credentials

    try:
        # Get the header to identify the right key
        header = jwt.get_unverified_header(token)
        key = next((k for k in JWKS if k["kid"] == header["kid"]), None)
        if key is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth key")

        # Verify and decode the token
        payload = jwt.decode(
            token,
            key=key["x5c"][0],
            algorithms=["RS256"],
            options={"verify_aud": False},  # Supabase JWT doesn't use audience by default
            issuer=f"{SUPABASE_URL}/auth/v1"
        )
        return payload

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token verification failed: {str(e)}")
