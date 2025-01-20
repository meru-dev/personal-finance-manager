from fastapi.requests import Request

from src.infrastructure.http_auth.common.ports.access_token_handler import (
    AccessTokenHandler,
)


class RequestHandler(AccessTokenHandler):
    def __init__(self, request: Request):
        self.request = request

    def get_access_token(self) -> str | None:
        authorization = self.request.headers.get("Authorization")
        if authorization and authorization.startswith("Bearer "):
            return authorization.split(" ")[-1]
        return None
