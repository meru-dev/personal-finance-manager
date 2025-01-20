from src.application.common.exceptions.base import ApplicationError
from src.domain.user.value_objects import Email, UserId, Username


class UserNotFoundByIdError(ApplicationError):
    def __init__(self, user_id: UserId):
        super().__init__(f"User with id {user_id} is not found")


class UsernameAlreadyExistsError(ApplicationError):
    def __init__(self, username: Username):
        super().__init__(f"Username {username} already exists")


class EmailAlreadyExistsError(ApplicationError):
    def __init__(self, email: Email):
        super().__init__(f"Email {email} already taken")


class WrongCredentialsError(ApplicationError):
    def __init__(self):
        super().__init__("Invalid username or password")
