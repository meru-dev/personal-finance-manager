from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette import status

from src.application.auth.token_interactor import (
    TokenData,
    TokenInteractor,
    TokenResult,
)
from src.presentation.api.common.schemas import SuccessResponse
from src.presentation.api.common.utils import error_responses

token_router = APIRouter()


class TokenResponse(SuccessResponse):
    details: TokenResult


@token_router.post(
    "/tokens",
    status_code=status.HTTP_200_OK,
    responses=error_responses(
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    ),
)
@inject
async def tokens(
    token_data: TokenData,
    interactor: FromDishka[TokenInteractor],
) -> TokenResponse:
    result = await interactor(token_data)
    return TokenResponse(details=result)
