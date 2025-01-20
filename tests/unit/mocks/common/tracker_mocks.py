from src.domain.common.tracker import Tracker
from src.domain.user.entity import User
from tests.unit.mocks.mappers.user_mapper_mock import UserMapperMock


class UserTrackerMock(Tracker):
    def __init__(self, user_mapper_mock: UserMapperMock):
        self._mapper_mock = user_mapper_mock

    async def add(self, user: User) -> None:
        await self._mapper_mock.save(user)

    async def add_many(self, users: list[User]) -> None:
        for user in users:
            await self._mapper_mock.save(user)

    async def delete(self, user: User) -> None:
        self._mapper_mock.user_storage.pop(user.id_)
