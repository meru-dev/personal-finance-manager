from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

http_bearer = HTTPBearer()


def auth_token(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> str:
    return credentials.credentials
