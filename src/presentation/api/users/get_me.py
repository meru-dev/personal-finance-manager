from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette import status

from src.application.users.get_me_interactor import (
    GetMeInteractor,
    GetMeResult,
)
from src.presentation.api.common.schemas import SuccessResponse
from src.presentation.api.common.utils import error_responses

get_me_router = APIRouter()


class GetMeResponse(SuccessResponse):
    details: GetMeResult


@get_me_router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    responses=error_responses(
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    ),
)
@inject
async def get_me(
    interactor: FromDishka[GetMeInteractor],
) -> GetMeResponse:
    result = await interactor()
    return GetMeResponse(details=result)
