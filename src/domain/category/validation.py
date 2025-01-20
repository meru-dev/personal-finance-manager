from typing import Final

from src.domain.category.exception import CategoryValidationError

CATEGORY_MIN_LEN: Final[int] = 1
CATEGORY_MAX_LEN: Final[int] = 50

CATEGORY_DESC_MAX_LEN: Final[int] = 50


def validate_category_name(name: str) -> None:
    if not CATEGORY_MIN_LEN <= len(name) <= CATEGORY_MAX_LEN:
        raise CategoryValidationError(
            f"Category name must be between "
            f"{CATEGORY_MIN_LEN} and "
            f"{CATEGORY_MAX_LEN} characters.",
        )


def validate_category_description(description: str | None) -> None:
    if description is None:
        return

    if not len(description) <= CATEGORY_DESC_MAX_LEN:
        raise CategoryValidationError(
            f"Category description must be "
            f"less than {CATEGORY_DESC_MAX_LEN} characters.",
        )
