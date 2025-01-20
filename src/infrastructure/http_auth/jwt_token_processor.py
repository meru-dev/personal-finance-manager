import uuid
from datetime import UTC, datetime
from enum import StrEnum, auto
from typing import Any, cast

import jwt

from src.domain.user.value_objects import UserId, Username
from src.infrastructure.http_auth.common.auth_session import (
    AuthSession,
    TokenId,
)
from src.setup.config import JWTAuthConfig


class TokenType(StrEnum):
    access = auto()
    refresh = auto()


class JwtTokenProcessor:
    def __init__(self, jwt_settings: JWTAuthConfig):
        self.jwt_settings = jwt_settings

    def _issue_token(self, token_type: TokenType, data: dict[str, Any]) -> str:
        payload = data.copy()
        payload["type"] = token_type
        return jwt.encode(
            payload,
            self.jwt_settings.private_key.read_text(),
            self.jwt_settings.algorithm,
        )

    def create_auth_session(self, user_id: UserId) -> AuthSession:
        now = datetime.now(tz=UTC)
        expire_at = now + self.jwt_settings.refresh_expire_days

        return AuthSession(
            id_=TokenId(uuid.uuid4()),
            user_id=user_id,
            expired_at=expire_at,
        )

    def issue_access_token(self, user_id: UserId, username: Username) -> str:
        now = datetime.now(tz=UTC)
        expire = now + self.jwt_settings.access_expire_minutes
        data = {
            "sub": str(user_id),
            "name": username,
            "jti": str(uuid.uuid4()),
            "exp": expire,
            "iat": now,
        }
        return self._issue_token(TokenType.access, data)

    def issue_refresh_token(self, auth_session: AuthSession) -> str:
        now = datetime.now(tz=UTC)
        data = {
            "sub": str(auth_session.user_id),
            "exp": auth_session.expired_at,
            "iat": now,
            "jti": str(auth_session.id_),
        }
        return self._issue_token(TokenType.refresh, data)

    def decode_jwt_token(self, token: str | bytes) -> dict[str, Any] | None:
        # jwt automatically validate sub, exp, iat, jti
        try:
            return cast(
                dict[str, Any],
                jwt.decode(
                    jwt=token,
                    key=self.jwt_settings.public_key.read_text(),
                    algorithms=[self.jwt_settings.algorithm],
                ),
            )

        except jwt.InvalidTokenError:
            return None

    def extract_type_from_token(
        self, decoded_token: dict[str, Any]
    ) -> TokenType | None:
        return decoded_token.get("type")

    def extract_user_id_from_token(
        self, decoded_token: dict[str, Any]
    ) -> UserId | None:
        sub = decoded_token.get("sub")
        if sub is None:
            return sub
        return UserId(uuid.UUID(sub))

    def extract_jti_from_token(
        self, decoded_token: dict[str, Any]
    ) -> TokenId | None:
        jti = decoded_token.get("jti")
        if jti is None:
            return jti
        return TokenId(uuid.UUID(jti))
