from datetime import datetime
from decimal import Decimal
from enum import StrEnum, auto
from typing import NewType

TransactionId = NewType("TransactionId", int)
TransactionName = NewType("TransactionName", str)


class TransactionType(StrEnum):
    INCOME = auto()
    EXPENSE = auto()


TransactionAmount = NewType("TransactionAmount", Decimal)
TransactionDate = NewType("TransactionDate", datetime)

TransactionPeriod = NewType("TransactionPeriod", int)
TransactionEndDate = NewType("TransactionEndDate", datetime)
