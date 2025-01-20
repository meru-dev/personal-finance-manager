from abc import abstractmethod
from typing import Protocol

from src.domain.user.value_objects import UserId


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_current(self) -> UserId:
        raise NotImplementedError

    @abstractmethod
    async def ensure_has_no_authentication(self) -> None:
        raise NotImplementedError
