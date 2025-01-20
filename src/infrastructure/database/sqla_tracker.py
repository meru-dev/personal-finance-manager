from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.common.tracker import Tracker


class SQLATracker(Tracker):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, entity: Any) -> None:
        return self._session.add(entity)

    async def add_many(self, entities: list[Any]) -> None:
        return self._session.add_all(entities)

    async def delete(self, entity: Any) -> None:
        return await self._session.delete(entity)
