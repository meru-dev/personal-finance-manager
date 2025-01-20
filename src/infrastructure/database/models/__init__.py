from .auth_session import map_auth_sessions_table
from .category import map_category_table
from .transaction import map_transaction_table
from .user import map_user_table

__all__ = ["map_tables"]


def map_tables() -> None:
    map_user_table()
    map_category_table()
    map_transaction_table()
    map_auth_sessions_table()
