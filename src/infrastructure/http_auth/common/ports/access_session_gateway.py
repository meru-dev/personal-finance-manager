from abc import abstractmethod
from typing import Protocol

from src.infrastructure.http_auth.common.auth_session import (
    AuthSession,
    TokenId,
)


class AuthSessionGateway(Protocol):
    @abstractmethod
    async def save(self, auth_session: AuthSession) -> None: ...

    @abstractmethod
    async def get_by_id(self, token_id: TokenId) -> AuthSession | None: ...

    @abstractmethod
    async def delete(self, auth_session: AuthSession) -> None: ...
