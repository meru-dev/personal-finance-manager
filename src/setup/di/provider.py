from collections.abc import Sequence

from dishka import Provider, Scope
from dotenv import load_dotenv

from src.application.auth.log_in_interactor import LogInInteractor
from src.application.auth.sign_up_interactor import SignUpInteractor
from src.application.auth.token_interactor import TokenInteractor
from src.application.common.ports.auth_manager import AuthManager
from src.application.common.ports.commiter import Commiter
from src.application.common.ports.identity_provider import IdentityProvider
from src.application.common.ports.user_gateway import UserGateway
from src.application.users.get_me_interactor import GetMeInteractor
from src.domain.category.service import CategoryService
from src.domain.common.ports.password_hasher import PasswordHasher
from src.domain.common.tracker import Tracker
from src.domain.transaction.service import TransactionService
from src.domain.user.service import UserService
from src.infrastructure.bcrypt_password_hasher import BcryptPasswordHasher
from src.infrastructure.database.gateways.auth_session import AuthSessionMapper
from src.infrastructure.database.gateways.user import UserMapper
from src.infrastructure.database.session import (
    get_async_session,
    get_async_sessionmaker,
    get_engine,
)
from src.infrastructure.database.sqla_commiter import SQLACommiter
from src.infrastructure.database.sqla_tracker import SQLATracker
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)
from src.infrastructure.http_auth.common.ports.access_token_handler import (
    AccessTokenHandler,
)
from src.infrastructure.http_auth.http_auth_manager import HttpAuthManager
from src.infrastructure.http_auth.jwt_token_processor import JwtTokenProcessor
from src.infrastructure.http_auth.request_handler import RequestHandler
from src.infrastructure.http_auth.user_identity_provider import (
    UserIdentityProvider,
)
from src.setup.config import Config, DatabaseConfig, JWTAuthConfig


def get_config_provider() -> Provider:
    provider = Provider()

    load_dotenv()
    config = Config()

    provider.provide(
        lambda: config.postgres,
        scope=Scope.APP,
        provides=DatabaseConfig,
    )
    provider.provide(
        lambda: config.auth_jwt,
        scope=Scope.APP,
        provides=JWTAuthConfig,
    )
    return provider


def get_adapters_provider() -> Provider:
    provider = Provider()

    provider.provide(get_engine, scope=Scope.APP)
    provider.provide(get_async_sessionmaker, scope=Scope.APP)
    provider.provide(get_async_session, scope=Scope.REQUEST)

    provider.provide(
        UserIdentityProvider,
        scope=Scope.REQUEST,
        provides=IdentityProvider,
    )
    provider.provide(
        HttpAuthManager,
        scope=Scope.REQUEST,
        provides=AuthManager,
    )
    provider.provide(JwtTokenProcessor, scope=Scope.REQUEST)
    provider.provide(
        RequestHandler,
        scope=Scope.REQUEST,
        provides=AccessTokenHandler,
    )

    return provider


def get_mapper_provider() -> Provider:
    provider = Provider()

    provider.provide(SQLACommiter, scope=Scope.REQUEST, provides=Commiter)
    provider.provide(SQLATracker, scope=Scope.REQUEST, provides=Tracker)

    provider.provide(UserMapper, scope=Scope.REQUEST, provides=UserGateway)
    provider.provide(
        AuthSessionMapper,
        scope=Scope.REQUEST,
        provides=AuthSessionGateway,
    )

    return provider


def get_interactor_provider() -> Provider:
    provider = Provider()

    provider.provide(SignUpInteractor, scope=Scope.REQUEST)
    provider.provide(LogInInteractor, scope=Scope.REQUEST)
    provider.provide(GetMeInteractor, scope=Scope.REQUEST)
    provider.provide(TokenInteractor, scope=Scope.REQUEST)

    return provider


def get_application_services_provider() -> Provider:
    provider = Provider()

    provider.provide(
        BcryptPasswordHasher,
        scope=Scope.SESSION,
        provides=PasswordHasher,
    )

    return provider


def get_domain_services_provider() -> Provider:
    provider = Provider()

    provider.provide(UserService, scope=Scope.REQUEST)
    provider.provide(CategoryService, scope=Scope.REQUEST)
    provider.provide(TransactionService, scope=Scope.REQUEST)

    return provider


def get_all_providers() -> Sequence[Provider]:
    return (
        get_adapters_provider(),
        get_config_provider(),
        get_mapper_provider(),
        get_interactor_provider(),
        get_application_services_provider(),
        get_domain_services_provider(),
    )
