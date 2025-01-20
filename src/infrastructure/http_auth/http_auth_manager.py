from src.application.common.exceptions.user import UserNotFoundByIdError
from src.application.common.ports.auth_manager import AuthManager
from src.application.common.ports.user_gateway import UserGateway
from src.domain.user.value_objects import UserId, Username
from src.infrastructure.http_auth.common.exceptions import (
    AccessTokenError,
    AuthenticationError,
    RefreshTokenError,
)
from src.infrastructure.http_auth.common.ports.access_session_gateway import (
    AuthSessionGateway,
)
from src.infrastructure.http_auth.common.ports.access_token_handler import (
    AccessTokenHandler,
)
from src.infrastructure.http_auth.jwt_token_processor import (
    JwtTokenProcessor,
    TokenType,
)


class HttpAuthManager(AuthManager):
    def __init__(
        self,
        token_processor: JwtTokenProcessor,
        token_request_handler: AccessTokenHandler,
        auth_session_gateway: AuthSessionGateway,
        user_gateway: UserGateway,
    ):
        self.token_processor = token_processor
        self.token_request_handler = token_request_handler
        self.auth_session_gateway = auth_session_gateway
        self.user_gateway = user_gateway

    async def validate_access(self) -> UserId:
        access_token = self.token_request_handler.get_access_token()
        if access_token is None:
            raise AuthenticationError

        decoded_token = self.token_processor.decode_jwt_token(access_token)
        if not decoded_token:
            raise AccessTokenError

        token_type = self.token_processor.extract_type_from_token(
            decoded_token,
        )
        if token_type != TokenType.access:
            raise AccessTokenError

        user_id = self.token_processor.extract_user_id_from_token(
            decoded_token,
        )
        if user_id is None:
            raise AccessTokenError

        return user_id

    async def create_auth_session(
        self,
        user_id: UserId,
        username: Username,
    ) -> tuple[str, str]:
        auth_session = self.token_processor.create_auth_session(user_id)
        access_token = self.token_processor.issue_access_token(
            user_id,
            username,
        )
        refresh_token = self.token_processor.issue_refresh_token(auth_session)
        await self.auth_session_gateway.save(auth_session)
        return access_token, refresh_token

    async def recreate_auth_session(
        self,
        refresh_token: str,
    ) -> tuple[str, str]:
        decoded_token = self.token_processor.decode_jwt_token(refresh_token)
        if not decoded_token:
            raise RefreshTokenError

        decoded_token_type = self.token_processor.extract_type_from_token(
            decoded_token,
        )
        if decoded_token_type != TokenType.refresh:
            raise RefreshTokenError

        user_id = self.token_processor.extract_user_id_from_token(
            decoded_token,
        )
        if user_id is None:
            raise RefreshTokenError

        token_id = self.token_processor.extract_jti_from_token(decoded_token)
        if token_id is None:
            raise RefreshTokenError

        auth_session = await self.auth_session_gateway.get_by_id(token_id)
        if auth_session is None:
            raise RefreshTokenError

        user = await self.user_gateway.read_by_id(user_id)
        if user is None or user.is_active is False:
            raise UserNotFoundByIdError(user_id)

        new_auth_session = self.token_processor.create_auth_session(user_id)
        new_access_token = self.token_processor.issue_access_token(
            user_id,
            user.username,
        )
        new_refresh_token = self.token_processor.issue_refresh_token(
            new_auth_session,
        )

        await self.auth_session_gateway.save(new_auth_session)
        await self.auth_session_gateway.delete(auth_session)

        return new_access_token, new_refresh_token
