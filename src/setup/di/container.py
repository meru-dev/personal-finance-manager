from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider

from src.setup.di.provider import get_all_providers


def make_container() -> AsyncContainer:
    return make_async_container(
        *get_all_providers(),
        FastapiProvider(),
    )
