from . import models
from .crud import crud_category
from .exceptions import CategoryNotFound


async def create_food_category(db, *, category_in) -> models.Category:
    """Create new food category in db"""

    return crud_category.create(db, obj_in=category_in)


async def get_food_category(db, *, category_id: int) -> models.Category:
    """Get a new food category by id from db"""
    category = crud_category.get(db, id=category_id)

    if not category:
        raise CategoryNotFound()

    return category


async def get_all_categories(db) -> list[models.Category]:
    """Get all food categories from db"""

    return crud_category.get_multi(db)
