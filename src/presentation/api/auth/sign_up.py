from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, status

from src.application.auth.sign_up_interactor import (
    SignUpData,
    SignUpInteractor,
    SignUpResult,
)
from src.presentation.api.common.schemas import SuccessResponse
from src.presentation.api.common.utils import error_responses

sign_up_router = APIRouter()


class SignUpResponse(SuccessResponse):
    details: SignUpResult


@sign_up_router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    responses=error_responses(
        status.HTTP_409_CONFLICT,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    ),
)
@inject
async def sign_up(
    request_data: SignUpData,
    interactor: FromDishka[SignUpInteractor],
) -> SignUpResponse:
    result = await interactor(request_data)
    return SignUpResponse(details=result)
