from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.infrastructure.database.models import map_tables
from src.presentation.api.common.exceptions import EXCEPTION_MAPPING, handler
from src.presentation.api.common.routers.root import root_router
from src.setup.di.container import make_container


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    # map database models to entities
    map_tables()
    yield
    await app.state.dishka_container.close()


def create_app() -> FastAPI:
    # setup app
    app = FastAPI(
        name="Personal Finance Manager",
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )
    app.include_router(root_router)

    # setup_exceptions to app
    for exception_class in EXCEPTION_MAPPING:
        app.add_exception_handler(exception_class, handler)

    # setup di
    setup_dishka(make_container(), app)
    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=create_app(), loop="uvloop")
