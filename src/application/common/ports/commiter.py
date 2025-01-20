from abc import abstractmethod
from typing import Protocol


class Commiter(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def flush(self) -> None:
        raise NotImplementedError
