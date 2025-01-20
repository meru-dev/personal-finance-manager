import pytest

from src.domain.user.exception import UsernameValidationError
from src.domain.user.validation import (
    USERNAME_MAX_LEN,
    USERNAME_MIN_LEN,
    validate_username,
)

_valid_usernames = [
    # length
    "u" * USERNAME_MIN_LEN,
    "u" * USERNAME_MAX_LEN,
    "u"
    * (USERNAME_MIN_LEN + round((USERNAME_MAX_LEN - USERNAME_MIN_LEN) / 2)),
    # chars
    "usernameaz",
    "USERNAMEAZ",
    "1234567890",
    # specials
    "user.name",
    "user-name",
    "user_name",
]

_invalid_usernames = [
    # length
    "",
    "u" * (USERNAME_MIN_LEN - 1),
    "u" * (USERNAME_MAX_LEN + 1),
    "u" * (USERNAME_MAX_LEN + 2),
    # chars
    "user@name",
    "user\x00name",
    "user name",
    "user\nname",
    # start and end with special chars
    ".username",
    "-username",
    "_username",
    "username.",
    "username-",
    "username_",
    # consecutive specials
    "user..name",
    "user--name",
    "user__name",
]


@pytest.mark.parametrize("valid_username", _valid_usernames)
def test_valid_username_validation(valid_username: str) -> None:
    validate_username(valid_username)


@pytest.mark.parametrize("invalid_username", _invalid_usernames)
def test_invalid_username_validation(invalid_username: str) -> None:
    with pytest.raises(UsernameValidationError):
        validate_username(invalid_username)
