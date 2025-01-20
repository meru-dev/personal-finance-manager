from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    func,
)
from sqlalchemy.orm import relationship

from src.domain.category.entity import Category
from src.domain.category.validation import (
    CATEGORY_DESC_MAX_LEN,
    CATEGORY_MAX_LEN,
)
from src.infrastructure.database.models.base import mapper_registry

categories_table = Table(
    "categories",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(CATEGORY_MAX_LEN), nullable=False),
    Column("description", String(CATEGORY_DESC_MAX_LEN), nullable=True),
    Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
    ),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column(
        "updated_at",
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
)


def map_category_table() -> None:
    mapper_registry.map_imperatively(
        Category,
        categories_table,
        properties={
            "id_": categories_table.c.id,
            "name": categories_table.c.name,
            "description": categories_table.c.description,
            "user_id": categories_table.c.user_id,
            "user": relationship("User", back_populates="categories"),
            "transactions": relationship(
                "Transaction",
                back_populates="category",
            ),
        },
        column_prefix="_",
    )
