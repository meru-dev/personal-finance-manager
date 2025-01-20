from fastapi import APIRouter
from fastapi.params import Security

from src.presentation.api.common.fast_api_dependecies import auth_token
from src.presentation.api.users.get_me import get_me_router

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Security(auth_token)],
)

users_sub_routers = (get_me_router,)

for router in users_sub_routers:
    users_router.include_router(router)
