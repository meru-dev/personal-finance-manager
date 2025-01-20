from abc import abstractmethod
from asyncio import Protocol
from typing import Any


class Tracker(Protocol):
    @abstractmethod
    async def add(self, entity: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add_many(self, entities: list[Any]) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entity: Any) -> None:
        raise NotImplementedError
