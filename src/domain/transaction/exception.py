from src.application.common.exceptions.base import ApplicationError


class TransactionValidationError(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message)
