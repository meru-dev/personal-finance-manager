from collections.abc import AsyncGenerator, AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.setup.config import DatabaseConfig


async def get_engine(
    settings: DatabaseConfig,
) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(
        settings.get_connection_url(),
        future=True,
        echo=True,
    )

    yield engine

    await engine.dispose()


async def get_async_sessionmaker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        engine,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
    )


async def get_async_session(
    session_factory: async_sessionmaker[AsyncSession],
) -> AsyncIterable[AsyncSession]:
    async with session_factory() as session:
        yield session
