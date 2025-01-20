from abc import abstractmethod
from typing import Protocol

from src.domain.user.entity import User
from src.domain.user.value_objects import Email, UserId, Username


class UserGateway(Protocol):
    @abstractmethod
    async def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def read_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def read_by_username(self, username: Username) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def read_by_email(self, email: Email) -> User | None:
        raise NotImplementedError
