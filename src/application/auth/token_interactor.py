from dataclasses import dataclass

from src.application.common.interactor import Interactor
from src.application.common.ports.auth_manager import AuthManager
from src.application.common.ports.commiter import Commiter
from src.application.common.ports.identity_provider import IdentityProvider
from src.domain.user.service import UserService
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)


@dataclass
class TokenData:
    refresh_token: str


@dataclass
class TokenResult:
    access_token: str
    refresh_token: str


class TokenInteractor(Interactor[TokenData, TokenResult]):
    def __init__(
        self,
        idp: IdentityProvider,
        auth_manager: AuthManager,
        token_gateway: AuthSessionGateway,
        user_service: UserService,
        commiter: Commiter,
    ):
        self.idp = idp
        self.token_gateway = token_gateway
        self.user_service = user_service
        self.auth_manager = auth_manager
        self.commiter = commiter

    async def __call__(self, data: TokenData) -> TokenResult:
        await self.idp.ensure_has_no_authentication()

        access_tokens = await self.auth_manager.recreate_auth_session(
            data.refresh_token,
        )
        await self.commiter.commit()

        return TokenResult(access_tokens[0], access_tokens[1])
