from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette import status

from src.application.auth.log_in_interactor import (
    LogInData,
    LogInInteractor,
    LogInResult,
)
from src.presentation.api.common.schemas import SuccessResponse
from src.presentation.api.common.utils import error_responses

log_in_router = APIRouter()


class LogInResponse(SuccessResponse):
    details: LogInResult


@log_in_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    responses=error_responses(
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    ),
)
@inject
async def log_in(
    log_in_data: LogInData,
    interactor: FromDishka[LogInInteractor],
) -> LogInResponse:
    result = await interactor(log_in_data)
    return LogInResponse(details=result)
