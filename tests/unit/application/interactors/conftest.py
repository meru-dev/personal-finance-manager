import pytest

from src.domain.user.service import UserService
from src.infrastructure.bcrypt_password_hasher import BcryptPasswordHasher


@pytest.fixture(scope="session")
def bcrypt_password_hasher():
    return BcryptPasswordHasher()


@pytest.fixture
def user_service(user_tracker, bcrypt_password_hasher):
    return UserService(bcrypt_password_hasher, user_tracker)
