from src.infrastructure.http_auth.common.ports.access_token_handler import (
    AccessTokenHandler,
)


class RequestHandlerMock(AccessTokenHandler):
    def __init__(self, headers: dict[str, str] | None = None):
        self._request_headers: dict[str, str] = {}
        if headers is not None:
            self._request_headers.update(headers)

    def get_access_token(self) -> str | None:
        authorization = self._request_headers.get("Authorization")
        if authorization and authorization.startswith("Bearer "):
            return authorization.split(" ")[-1]
        return None
