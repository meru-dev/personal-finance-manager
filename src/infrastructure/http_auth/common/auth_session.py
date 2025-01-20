from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from src.domain.user.value_objects import UserId

TokenId = NewType("TokenId", UUID)
Token = NewType("Token", str)


@dataclass
class AuthSession:
    id_: TokenId
    user_id: UserId
    expired_at: datetime
