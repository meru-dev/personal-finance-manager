from dataclasses import dataclass

from src.application.common.exceptions.user import WrongCredentialsError
from src.application.common.interactor import Interactor
from src.application.common.ports.auth_manager import AuthManager
from src.application.common.ports.commiter import Commiter
from src.application.common.ports.identity_provider import IdentityProvider
from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.service import UserService
from src.domain.user.value_objects import RawPassword, Username


@dataclass
class LogInData:
    username: str
    password: str


@dataclass
class LogInResult:
    access_token: str
    refresh_token: str


class LogInInteractor(Interactor[LogInData, LogInResult]):
    def __init__(
        self,
        idp: IdentityProvider,
        auth_manager: AuthManager,
        user_gateway: UserGateway,
        user_service: UserService,
        commiter: Commiter,
    ):
        self.idp = idp
        self.user_gateway = user_gateway
        self.user_service = user_service
        self.auth_manager = auth_manager
        self.commiter = commiter

    async def __call__(self, data: LogInData) -> LogInResult:
        await self.idp.ensure_has_no_authentication()

        username = Username(data.username)
        password = RawPassword(data.password)

        user = await self.user_gateway.read_by_username(username)
        if user is None or not await self.user_service.is_active_user(user):
            raise WrongCredentialsError

        if not await self.user_service.is_valid_password(user, password):
            raise WrongCredentialsError

        (
            access_token,
            refresh_token,
        ) = await self.auth_manager.create_auth_session(
            user.id_,
            user.username,
        )
        await self.commiter.commit()

        return LogInResult(
            access_token=access_token,
            refresh_token=refresh_token,
        )
