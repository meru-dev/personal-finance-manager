from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.http_auth.common.auth_session import (
    AuthSession,
    TokenId,
)
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)


class AuthSessionMapper(AuthSessionGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, token_id: TokenId) -> AuthSession | None:
        return await self._session.get(AuthSession, token_id)

    async def save(self, auth_session: AuthSession) -> None:
        self._session.add(auth_session)

    async def delete(self, auth_session: AuthSession) -> None:
        await self._session.delete(auth_session)
