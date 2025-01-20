from dataclasses import dataclass

from src.application.common.exceptions.user import UserNotFoundByIdError
from src.application.common.ports.identity_provider import IdentityProvider
from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.value_objects import UserId


@dataclass
class GetMeResult:
    id: UserId
    username: str
    email: str


class GetMeInteractor:
    def __init__(
        self,
        ipd: IdentityProvider,
        user_reader: UserGateway,
    ):
        self.ipd = ipd
        self.user_reader = user_reader

    async def __call__(self) -> GetMeResult:
        current_user_id = await self.ipd.get_current()

        user = await self.user_reader.read_by_id(current_user_id)

        if user is None:
            raise UserNotFoundByIdError(current_user_id)

        return GetMeResult(
            id=user.id_,
            username=user.username,
            email=user.email,
        )
