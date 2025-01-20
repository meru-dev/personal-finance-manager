import uuid

from src.domain.common.ports.password_hasher import PasswordHasher
from src.domain.common.tracker import Tracker
from src.domain.user.entity import User
from src.domain.user.validation import (
    validate_email,
    validate_password,
    validate_username,
)
from src.domain.user.value_objects import (
    Email,
    Password,
    RawPassword,
    UserId,
    Username,
)


class UserService:
    def __init__(self, password_hasher: PasswordHasher, tracker: Tracker):
        self._password_hasher = password_hasher
        self._tracker = tracker

    async def create_user(
        self,
        username: Username,
        password: RawPassword,
        email: Email,
    ) -> User:
        validate_username(username)
        validate_password(password)
        validate_email(email)

        user = User(
            id_=UserId(uuid.uuid4()),
            username=username,
            password=Password(self._password_hasher.hash(password)),
            email=email,
            is_active=True,
        )
        await self._tracker.add(user)
        return user

    async def is_valid_password(
        self,
        user: User,
        password: RawPassword,
    ) -> bool:
        return self._password_hasher.verify(
            raw_password=password,
            password=user.password,
        )

    async def is_active_user(self, user: User) -> bool:
        return user.is_active
