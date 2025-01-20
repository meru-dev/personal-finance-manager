import re
from typing import Final

from src.domain.user.exception import (
    EmailValidationError,
    PasswordValidationError,
    UsernameValidationError,
)

USERNAME_MIN_LEN: Final[int] = 5
USERNAME_MAX_LEN: Final[int] = 20
USERNAME_ALLOWED_CHARS: Final[re.Pattern[str]] = re.compile(
    r"[a-zA-Z0-9._-]*",
)
USERNAME_START_AND_END_WITH_NO_SPECIALS: Final[re.Pattern[str]] = re.compile(
    r"^[a-zA-Z0-9].*[a-zA-Z0-9]$",
)
USERNAME_NO_CONSECUTIVE_SPECIALS: Final[re.Pattern[str]] = re.compile(
    r"^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*[._-]?$",
)

PASSWORD_MIN_LEN: Final[int] = 8
PASSWORD_MAX_LEN: Final[int] = 64
PASSWORD_CONTAINS_AT_LEAST_ONE_UPPERCASE: Final[re.Pattern[str]] = re.compile(
    r"[A-Z]",
)
PASSWORD_CONTAINS_AT_LEAST_ONE_LOWERCASE: Final[re.Pattern[str]] = re.compile(
    r"[a-z]",
)
PASSWORD_CONTAINS_AT_LEAST_ONE_DIGIT: Final[re.Pattern[str]] = re.compile(
    r"\d",
)
PASSWORD_CONTAINS_AT_LEAST_ONE_SPECIAL: Final[re.Pattern[str]] = re.compile(
    r"[@$!%*?&]",
)

EMAIL_MIN_LEN: Final[int] = 5
EMAIL_MAX_LEN: Final[int] = 255
EMAIL_IS_CORRECT: Final[re.Pattern[str]] = re.compile(
    r"^(?!\.)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+$",
)


def validate_username(username: str) -> None:
    if not USERNAME_MIN_LEN <= len(username) <= USERNAME_MAX_LEN:
        raise UsernameValidationError(
            f"Username must be between "
            f"{USERNAME_MIN_LEN} and "
            f"{USERNAME_MAX_LEN} characters.",
        )

    if not re.fullmatch(USERNAME_ALLOWED_CHARS, username):
        raise UsernameValidationError(
            "Username should only contain letters (A-Z, a-z), digits (0-9), "
            "dots (.), hyphens (-), and underscores (_).",
        )

    if not re.fullmatch(USERNAME_START_AND_END_WITH_NO_SPECIALS, username):
        raise UsernameValidationError(
            "Username should only start and "
            "end with letters (A-Z, a-z) and digits (0-9).",
        )

    if not re.fullmatch(USERNAME_NO_CONSECUTIVE_SPECIALS, username):
        raise UsernameValidationError(
            "Username cannot contain consecutive "
            "special characters like .., --, or __.",
        )


def validate_password(password: str) -> None:
    if not PASSWORD_MIN_LEN <= len(password) <= PASSWORD_MAX_LEN:
        raise PasswordValidationError(
            f"Password must be between "
            f"{PASSWORD_MIN_LEN} and "
            f"{PASSWORD_MAX_LEN} characters.",
        )

    if not re.search(PASSWORD_CONTAINS_AT_LEAST_ONE_UPPERCASE, password):
        raise PasswordValidationError(
            "Password should contain at least one CAPITAL letter.",
        )

    if not re.search(PASSWORD_CONTAINS_AT_LEAST_ONE_LOWERCASE, password):
        raise PasswordValidationError(
            "Password should contain at least one LOWER letter.",
        )

    if not re.search(PASSWORD_CONTAINS_AT_LEAST_ONE_DIGIT, password):
        raise PasswordValidationError(
            "Password should contain at least one DIGIT.",
        )

    if not re.search(PASSWORD_CONTAINS_AT_LEAST_ONE_SPECIAL, password):
        raise PasswordValidationError(
            "Password should contain at least "
            "one of the special characters: @$!%*?&",
        )


def validate_email(email: str) -> None:
    if not EMAIL_MIN_LEN <= len(email) <= EMAIL_MAX_LEN:
        raise EmailValidationError(
            f"Email must be between "
            f"{EMAIL_MIN_LEN} and "
            f"{EMAIL_MAX_LEN} characters.",
        )

    if not re.fullmatch(EMAIL_IS_CORRECT, email):
        raise EmailValidationError(
            "Email should be correct format (e.g., user@example.com)",
        )
