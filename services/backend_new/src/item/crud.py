from sqlalchemy.orm import Session
from src.category.services import get_food_category
from src.utils.curd_base import CRUDBase

from .models import Item
from .schemas import ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    """Item specific crud opertations"""

    async def create(self, db: Session, *, obj_in: ItemCreate) -> Item:
        # check the category exists or not
        await get_food_category(db, category_id=obj_in.category_id)

        return super().create(db, obj_in=obj_in)


crud_item = CRUDItem(Item)
