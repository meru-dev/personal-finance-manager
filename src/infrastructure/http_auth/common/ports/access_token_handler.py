from abc import abstractmethod
from typing import Protocol


class AccessTokenHandler(Protocol):
    @abstractmethod
    def get_access_token(self) -> str | None: ...
