from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.food import FoodCategory, FoodItem
from src.schemas.food import (
    FoodCategoryCreate,
    FoodCategoryUpdate,
    FoodItemCreate,
    FoodItemUpdate,
)


class CRUDFoodItem(CRUDBase[FoodItem, FoodItemCreate, FoodItemUpdate]):
    def get_food_items_by_category(self, db: Session, *, category_id: int):
        """Get all food items under a category"""
        return (
            db.query(FoodItem)
            .join(FoodCategory)
            .filter(FoodCategory.category_id == category_id)
            .all()
        )


CRUDFoodCategory = CRUDBase[FoodCategory, FoodCategoryCreate, FoodCategoryUpdate]

crud_food_category = CRUDFoodCategory(FoodCategory)
crud_food_item = CRUDFoodItem(FoodItem)
