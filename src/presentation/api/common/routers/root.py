from fastapi import APIRouter

from src.presentation.api.common.routers.api_v1 import api_v1_router

root_router = APIRouter()

root_sub_routers = (api_v1_router,)

for router in root_sub_routers:
    root_router.include_router(router)
