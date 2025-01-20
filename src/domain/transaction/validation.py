from typing import Final

from src.domain.transaction.exception import TransactionValidationError

TRANSACTION_MIN_LEN: Final[int] = 1
TRANSACTION_MAX_LEN: Final[int] = 50


def validate_transaction_name(name: str) -> None:
    if not TRANSACTION_MIN_LEN <= len(name) <= TRANSACTION_MAX_LEN:
        raise TransactionValidationError(
            f"Transaction name must be between "
            f"{TRANSACTION_MIN_LEN} and "
            f"{TRANSACTION_MAX_LEN} characters.",
        )
