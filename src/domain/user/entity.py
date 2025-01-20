from dataclasses import dataclass

from src.domain.user.value_objects import Email, Password, UserId, Username


@dataclass
class User:
    id_: UserId
    username: Username
    password: Password
    email: Email
    is_active: bool
