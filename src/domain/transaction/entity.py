from dataclasses import dataclass

from src.domain.category.value_objects import CategoryId
from src.domain.transaction.value_objects import (
    TransactionAmount,
    TransactionDate,
    TransactionEndDate,
    TransactionId,
    TransactionName,
    TransactionPeriod,
    TransactionType,
)
from src.domain.user.value_objects import UserId


@dataclass
class Transaction:
    id_: TransactionId | None
    name: TransactionName
    type: TransactionType
    amount: TransactionAmount
    date: TransactionDate
    period: TransactionPeriod | None
    end_date: TransactionEndDate | None

    user_id: UserId
    category_id: CategoryId | None
