from dataclasses import dataclass
from uuid import UUID

from src.application.common.exceptions.user import (
    EmailAlreadyExistsError,
    UsernameAlreadyExistsError,
)
from src.application.common.interactor import Interactor
from src.application.common.ports.commiter import Commiter
from src.application.common.ports.identity_provider import IdentityProvider
from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.service import UserService
from src.domain.user.value_objects import Email, RawPassword, Username


@dataclass
class SignUpData:
    username: str
    password: str
    email: str


@dataclass
class SignUpResult:
    user_id: UUID
    username: str
    email: str


class SignUpInteractor(Interactor[SignUpData, SignUpResult]):
    def __init__(
        self,
        idp: IdentityProvider,
        user_gateway: UserGateway,
        user_service: UserService,
        commiter: Commiter,
    ):
        self.idp = idp
        self.user_gateway = user_gateway
        self.user_service = user_service
        self.commiter = commiter

    async def __call__(self, sign_up_data: SignUpData) -> SignUpResult:
        await self.idp.ensure_has_no_authentication()

        username = Username(sign_up_data.username)
        password = RawPassword(sign_up_data.password)
        email = Email(sign_up_data.email)

        user_by_username = await self.user_gateway.read_by_username(username)
        if user_by_username:
            raise UsernameAlreadyExistsError(username)

        user_by_email = await self.user_gateway.read_by_email(email)
        if user_by_email:
            raise EmailAlreadyExistsError(email)

        user = await self.user_service.create_user(
            username=username,
            password=password,
            email=email,
        )

        await self.commiter.commit()
        return SignUpResult(user.id_, user.username, user.email)
