from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.entity import User
from src.domain.user.value_objects import Email, UserId, Username


class UserMapperMock(UserGateway):
    def __init__(self):
        self.user_storage: dict[UserId, User] = {}

    async def save(self, user: User) -> None:
        self.user_storage[user.id_] = user

    async def read_by_id(self, user_id: UserId) -> User | None:
        return self.user_storage.get(user_id)

    async def read_by_username(self, username: Username) -> User | None:
        for user in self.user_storage.values():
            if user.username == username:
                return user
        return None

    async def read_by_email(self, email: Email) -> User | None:
        for user in self.user_storage.values():
            if user.email == email:
                return user
        return None
