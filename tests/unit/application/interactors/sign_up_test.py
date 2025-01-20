import uuid

from src.application.auth.sign_up_interactor import (
    SignUpData,
    SignUpInteractor,
)
from src.domain.user.service import UserService
from src.domain.user.value_objects import UserId
from tests.unit.mocks.common.commiter_mock import CommiterMock
from tests.unit.mocks.common.user_identity_provider_mock import (
    UserIdentityProviderMock,
)
from tests.unit.mocks.mappers.user_mapper_mock import UserMapperMock


async def test_sign_up_success(
    user_mapper: UserMapperMock,
    user_service: UserService,
    commiter: CommiterMock,
    idp: UserIdentityProviderMock,
) -> None:
    username = "merudesu"
    password = "Pa$$w0rd"
    email = "meru@gmail.com"
    data = SignUpData(username=username, password=password, email=email)
    interactor = SignUpInteractor(idp, user_mapper, user_service, commiter)

    result = await interactor(data)

    assert isinstance(result.user_id, uuid.UUID)
    assert result.username == username
    assert result.email == email

    user = await user_mapper.read_by_id(UserId(result.user_id))

    assert user is not None
    assert user.username == username
    assert user.email == email

    assert commiter.commited is True
