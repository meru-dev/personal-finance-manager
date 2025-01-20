from src.application.common.ports.auth_manager import AuthManager
from src.application.common.ports.identity_provider import IdentityProvider
from src.domain.user.value_objects import UserId
from src.infrastructure.http_auth.common.exceptions import (
    AlreadyAuthenticatedError,
    AuthenticationError,
)


class UserIdentityProvider(IdentityProvider):
    def __init__(self, auth_manager: AuthManager):
        self.auth_manager = auth_manager

    async def get_current(self) -> UserId:
        return await self.auth_manager.validate_access()

    async def ensure_has_no_authentication(self) -> None:
        try:
            await self.get_current()
            raise AlreadyAuthenticatedError
        except AuthenticationError:
            pass
