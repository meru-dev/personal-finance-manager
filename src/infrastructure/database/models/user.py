from sqlalchemy import (
    UUID,
    Boolean,
    Column,
    DateTime,
    LargeBinary,
    String,
    Table,
    func,
)
from sqlalchemy.orm import relationship

from src.domain.user.entity import User
from src.domain.user.validation import EMAIL_MAX_LEN, USERNAME_MAX_LEN
from src.infrastructure.database.models.base import mapper_registry

users_table = Table(
    "users",
    mapper_registry.metadata,
    Column("id", UUID, primary_key=True, index=True),
    Column("username", String(USERNAME_MAX_LEN), unique=True, nullable=False),
    Column("password", LargeBinary, nullable=False),
    Column("email", String(EMAIL_MAX_LEN), unique=True, nullable=False),
    Column("is_active", Boolean, default=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column(
        "updated_at",
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
)


def map_user_table() -> None:
    mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "id_": users_table.c.id,
            "username": users_table.c.username,
            "password": users_table.c.password,
            "email": users_table.c.email,
            "is_active": users_table.c.is_active,
            "auth_sessions": relationship(
                "AuthSession",
                back_populates="user",
                cascade="all, delete-orphan",
            ),
            "categories": relationship(
                "Category",
                back_populates="user",
                cascade="all, delete-orphan",
            ),
            "transactions": relationship(
                "Transaction",
                back_populates="user",
                cascade="all, delete-orphan",
            ),
        },
        column_prefix="_",
    )
