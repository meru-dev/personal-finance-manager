from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.operators import eq

from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.entity import User
from src.domain.user.value_objects import Email, UserId, Username


class UserMapper(UserGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, user: User) -> None:
        self._session.add(user)

    async def read_by_id(self, user_id: UserId) -> User | None:
        return await self._session.get(User, user_id)

    async def read_by_username(self, username: Username) -> User | None:
        statement = select(User).where(
            eq(User.username, username),  # type: ignore
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()

    async def read_by_email(self, email: Email) -> User | None:
        statement = select(User).where(
            eq(User.email, email),  # type: ignore
        )
        result = await self._session.execute(statement)
        return result.scalar_one_or_none()
