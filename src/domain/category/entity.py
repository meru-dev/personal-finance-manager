from dataclasses import dataclass

from src.domain.category.value_objects import (
    CategoryDescription,
    CategoryId,
    CategoryName,
)
from src.domain.user.value_objects import UserId


@dataclass
class Category:
    id_: CategoryId | None
    name: CategoryName
    description: CategoryDescription | None
    user_id: UserId
