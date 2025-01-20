from abc import abstractmethod
from typing import Protocol

from src.domain.user.value_objects import Password, RawPassword


class PasswordHasher(Protocol):
    @abstractmethod
    def hash(self, raw_password: RawPassword) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def verify(self, raw_password: RawPassword, password: Password) -> bool:
        raise NotImplementedError
