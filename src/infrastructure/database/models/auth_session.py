from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    Table,
    func,
)
from sqlalchemy.orm import relationship

from src.infrastructure.database.models.base import mapper_registry
from src.infrastructure.http_auth.common.auth_session import AuthSession

auth_sessions_table = Table(
    "auth_sessions",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, index=True),
    Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("expired_at", DateTime(timezone=True), nullable=False),
    Column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    ),
)


def map_auth_sessions_table() -> None:
    mapper_registry.map_imperatively(
        AuthSession,
        auth_sessions_table,
        properties={
            "id_": auth_sessions_table.c.id,  # jti
            "user_id": auth_sessions_table.c.user_id,  # sub
            "expired_at": auth_sessions_table.c.expired_at,  # exp
            "user": relationship("User", back_populates="auth_sessions"),
        },
        column_prefix="_",
    )
