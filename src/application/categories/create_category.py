from dataclasses import dataclass

from src.application.common.exceptions.user import (
    EmailAlreadyExistsError,
    UsernameAlreadyExistsError,
)
from src.application.common.interactor import Interactor
from src.application.common.ports.commiter import Commiter
from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.service import UserService
from src.domain.user.value_objects import Email, RawPassword, UserId, Username


@dataclass
class RegisterUserData:
    username: str
    password: str
    email: str


@dataclass
class RegisterUserResult:
    user_id: UserId
    username: Username
    email: Email


class CreateCategoryInteractor(
    Interactor[RegisterUserData, RegisterUserResult],
):
    def __init__(
        self,
        user_gateway: UserGateway,
        user_service: UserService,
        commiter: Commiter,
    ):
        self.user_gateway = user_gateway
        self.user_service = user_service
        self.commiter = commiter

    async def __call__(
        self,
        register_user_data: RegisterUserData,
    ) -> RegisterUserResult:
        username = Username(register_user_data.username)
        password = RawPassword(register_user_data.password)
        email = Email(register_user_data.email)

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

        await self.user_gateway.save(user)
        await self.commiter.commit()

        return RegisterUserResult(user.id_, user.username, user.email)
