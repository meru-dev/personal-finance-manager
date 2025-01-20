from typing import Any

from src.presentation.api.common.schemas import ErrorResponse


def error_responses(
    *error_codes: int,
) -> dict[int | str, dict[str, Any]] | None:
    return {code: {"model": ErrorResponse} for code in error_codes}
