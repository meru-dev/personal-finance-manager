from fastapi import APIRouter

from src.presentation.api.common.routers.auth import auth_router
from src.presentation.api.common.routers.user import users_router

api_v1_router = APIRouter(
    prefix="/api/v1",
)

api_v1_sub_routers = (
    auth_router,
    users_router,
)

for router in api_v1_sub_routers:
    api_v1_router.include_router(router)
