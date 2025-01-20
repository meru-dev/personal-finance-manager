from enum import StrEnum
from typing import NewType
from uuid import UUID

UserId = NewType("UserId", UUID)
Username = NewType("Username", str)
Password = NewType("Password", bytes)
Email = NewType("Email", str)
RawPassword = NewType("RawPassword", str)


class UserRoleEnum(StrEnum):
    USER = "user"
    ADMIN = "admin"
