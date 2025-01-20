from src.domain.category.value_objects import CategoryId
from src.domain.common.tracker import Tracker
from src.domain.transaction.entity import Transaction
from src.domain.transaction.validation import validate_transaction_name
from src.domain.transaction.value_objects import (
    TransactionAmount,
    TransactionDate,
    TransactionEndDate,
    TransactionName,
    TransactionPeriod,
    TransactionType,
)
from src.domain.user.value_objects import UserId


class TransactionService:
    def __init__(self, tracker: Tracker):
        self._tracker = tracker

    async def new_transaction(
        self,
        user_id: UserId,
        name: TransactionName,
        ttype: TransactionType,
        amount: TransactionAmount,
        date: TransactionDate,
        period: TransactionPeriod | None = None,
        end_date: TransactionEndDate | None = None,
        category_id: CategoryId | None = None,
    ) -> Transaction:
        validate_transaction_name(name)

        transaction = Transaction(
            id_=None,
            user_id=user_id,
            name=name,
            type=ttype,
            amount=amount,
            date=date,
            period=period,
            end_date=end_date,
            category_id=category_id,
        )
        await self._tracker.add(transaction)
        return transaction
