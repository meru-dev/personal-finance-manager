from sqlalchemy import (
    DECIMAL,
    UUID,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    func,
)
from sqlalchemy.orm import relationship

from src.domain.transaction.entity import Transaction
from src.domain.transaction.validation import TRANSACTION_MAX_LEN
from src.domain.transaction.value_objects import TransactionType
from src.infrastructure.database.models.base import mapper_registry

transactions_table = Table(
    "transactions",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(TRANSACTION_MAX_LEN), nullable=False),
    Column("type", Enum(TransactionType), nullable=False),
    Column("amount", DECIMAL(scale=2), nullable=False),
    Column("date", DateTime(timezone=True), nullable=False),
    Column("period", Integer, nullable=True),
    Column("end_date", DateTime(timezone=True), nullable=True),
    Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
    ),
    Column(
        "category_id",
        Integer,
        ForeignKey("categories.id", ondelete="SET NULL"),
    ),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column(
        "updated_at",
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
)


def map_transaction_table() -> None:
    mapper_registry.map_imperatively(
        Transaction,
        transactions_table,
        properties={
            "id_": transactions_table.c.id,
            "name": transactions_table.c.name,
            "type": transactions_table.c.type,
            "amount": transactions_table.c.amount,
            "date": transactions_table.c.date,
            "period": transactions_table.c.period,
            "end_date": transactions_table.c.end_date,
            "user_id": transactions_table.c.user_id,
            "category_id": transactions_table.c.category_id,
            "user": relationship("User", back_populates="transactions"),
            "category": relationship(
                "Category",
                back_populates="transactions",
            ),
        },
        column_prefix="_",
    )
