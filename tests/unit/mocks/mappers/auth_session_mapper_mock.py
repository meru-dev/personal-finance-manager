from src.infrastructure.http_auth.common.auth_session import (
    AuthSession,
    TokenId,
)
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)


class AuthSessionMapperMock(AuthSessionGateway):
    def __init__(self):
        self._auth_session_storage: dict[TokenId, AuthSession] = {}

    async def get_by_id(self, token_id: TokenId) -> AuthSession | None:
        return self._auth_session_storage.get(token_id)

    async def save(self, auth_session: AuthSession) -> None:
        self._auth_session_storage[auth_session.id_] = auth_session

    async def delete(self, auth_session: AuthSession) -> None:
        self._auth_session_storage.pop(auth_session.id_)
