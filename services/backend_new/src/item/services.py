from . import models
from .crud import crud_item


async def create_food_item(db, *, item_in) -> models.Item:
    """Create a new food item in db"""

    return await crud_item.create(db, obj_in=item_in)
