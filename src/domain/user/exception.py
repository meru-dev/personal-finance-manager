from src.domain.common.exceptions import DomainError


class UsernameValidationError(DomainError):
    def __init__(self, message: str):
        super().__init__(message)


class PasswordValidationError(DomainError):
    def __init__(self, message: str):
        super().__init__(message)


class EmailValidationError(DomainError):
    def __init__(self, message: str):
        super().__init__(message)
