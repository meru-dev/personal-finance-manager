from abc import abstractmethod
from typing import Protocol

from src.domain.user.value_objects import UserId, Username


class AuthManager(Protocol):
    @abstractmethod
    async def validate_access(self) -> UserId:
        raise NotImplementedError

    @abstractmethod
    async def create_auth_session(
        self,
        user_id: UserId,
        username: Username,
    ) -> tuple[str, str]:
        raise NotImplementedError

    @abstractmethod
    async def recreate_auth_session(
        self,
        refresh_token: str,
    ) -> tuple[str, str]:
        raise NotImplementedError
