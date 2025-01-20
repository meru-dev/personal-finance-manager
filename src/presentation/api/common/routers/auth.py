from fastapi import APIRouter

from src.presentation.api.auth.log_in import log_in_router
from src.presentation.api.auth.sign_up import sign_up_router
from src.presentation.api.auth.tokens import token_router

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

auth_sub_routers = (
    sign_up_router,
    log_in_router,
    token_router,
)

for router in auth_sub_routers:
    auth_router.include_router(router)
