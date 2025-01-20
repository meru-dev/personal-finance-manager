import pytest

from src.infrastructure.http_auth.jwt_token_processor import JwtTokenProcessor
from src.setup.config import JWTAuthConfig
from tests.unit.mocks.common.commiter_mock import CommiterMock
from tests.unit.mocks.common.http_auth_manager_mock import HttpAuthManagerMock
from tests.unit.mocks.common.token_request_handler_mock import (
    RequestHandlerMock,
)
from tests.unit.mocks.common.tracker_mocks import UserTrackerMock
from tests.unit.mocks.common.user_identity_provider_mock import (
    UserIdentityProviderMock,
)
from tests.unit.mocks.mappers.auth_session_mapper_mock import (
    AuthSessionMapperMock,
)
from tests.unit.mocks.mappers.user_mapper_mock import UserMapperMock


@pytest.fixture
def user_mapper():
    return UserMapperMock()


@pytest.fixture
def commiter():
    return CommiterMock()


@pytest.fixture
def request_handler():
    return RequestHandlerMock()


@pytest.fixture
def jwt_token_processor():
    jwt_auth_settings = JWTAuthConfig()
    return JwtTokenProcessor(jwt_auth_settings)


@pytest.fixture
def auth_session_mapper():
    return AuthSessionMapperMock()


@pytest.fixture
def http_auth_manager(
    jwt_token_processor, request_handler, user_mapper, auth_session_mapper
):
    return HttpAuthManagerMock(
        jwt_token_processor, request_handler, auth_session_mapper, user_mapper
    )


@pytest.fixture
def idp(http_auth_manager):
    return UserIdentityProviderMock(http_auth_manager)


@pytest.fixture
def user_tracker(user_mapper):
    return UserTrackerMock(user_mapper)
