from src.domain.category.entity import Category
from src.domain.category.validation import (
    validate_category_description,
    validate_category_name,
)
from src.domain.category.value_objects import CategoryDescription, CategoryName
from src.domain.common.tracker import Tracker
from src.domain.user.value_objects import UserId


class CategoryService:
    def __init__(self, tracker: Tracker):
        self._tracker = tracker

    async def new_category(
        self,
        user_id: UserId,
        name: CategoryName,
        description: CategoryDescription | None,
    ) -> Category:
        validate_category_name(name)
        validate_category_description(description)

        category = Category(
            id_=None,
            name=name,
            description=description,
            user_id=user_id,
        )
        await self._tracker.add(category)
        return category
