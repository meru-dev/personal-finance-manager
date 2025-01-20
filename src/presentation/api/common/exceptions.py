from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse

from src.application.common.exceptions.user import (
    EmailAlreadyExistsError,
    UsernameAlreadyExistsError,
    UserNotFoundByIdError,
    WrongCredentialsError,
)
from src.domain.user.exception import (
    EmailValidationError,
    PasswordValidationError,
    UsernameValidationError,
)
from src.infrastructure.http_auth.common.exceptions import (
    AccessTokenError,
    AlreadyAuthenticatedError,
    AuthenticationError,
    RefreshTokenError,
)
from src.presentation.api.common.schemas import ErrorResponse

EXCEPTION_MAPPING: dict[type[Exception], int] = {
    # # 400
    # DomainFieldError: status.HTTP_400_BAD_REQUEST,
    # SortingError: status.HTTP_400_BAD_REQUEST,
    # 401
    WrongCredentialsError: status.HTTP_401_UNAUTHORIZED,
    AuthenticationError: status.HTTP_401_UNAUTHORIZED,
    AccessTokenError: status.HTTP_401_UNAUTHORIZED,
    AlreadyAuthenticatedError: status.HTTP_401_UNAUTHORIZED,
    # # 403
    # AuthorizationError: status.HTTP_403_FORBIDDEN,
    # # 404
    UserNotFoundByIdError: status.HTTP_404_NOT_FOUND,
    # UserNotFoundByUsername: status.HTTP_404_NOT_FOUND,
    # 409
    UsernameAlreadyExistsError: status.HTTP_409_CONFLICT,
    EmailAlreadyExistsError: status.HTTP_409_CONFLICT,
    # 422
    RequestValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    UsernameValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    PasswordValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    EmailValidationError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    RefreshTokenError: status.HTTP_422_UNPROCESSABLE_ENTITY,
}


async def handler(_: Request, exc: Exception) -> ORJSONResponse:
    status_code: int = EXCEPTION_MAPPING.get(
        type(exc),
        status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

    if isinstance(exc, RequestValidationError):
        details = jsonable_encoder(exc.errors())
        response = ErrorResponse(
            details=f"Request params not correspond to schema: {details}",
        )
    else:
        (message,) = exc.args
        response = ErrorResponse(details=message)

    return ORJSONResponse(
        status_code=status_code,
        content=response.model_dump(),
    )
