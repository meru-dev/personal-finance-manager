from src.application.common.ports.user_gateway import UserGateway
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)
from src.infrastructure.http_auth.common.ports.access_token_handler import (
    AccessTokenHandler,
)
from src.infrastructure.http_auth.http_auth_manager import HttpAuthManager
from src.infrastructure.http_auth.jwt_token_processor import (
    JwtTokenProcessor,
)


class HttpAuthManagerMock(HttpAuthManager):
    def __init__(
        self,
        token_processor: JwtTokenProcessor,
        token_request_handler: AccessTokenHandler,
        auth_session_gateway: AuthSessionGateway,
        user_gateway: UserGateway,
    ):
        super().__init__(
            token_processor,
            token_request_handler,
            auth_session_gateway,
            user_gateway,
        )
        self.token_processor = token_processor
        self.token_request_handler = token_request_handler
        self.auth_session_gateway = auth_session_gateway
        self.user_gateway = user_gateway
