from src.crud.base import CRUDBase
from src.models.food import FoodCategory
from src.schemas.food import FoodCategoryCreate, FoodCategoryUpdate

CRUDFoodCategory = CRUDBase[FoodCategory, FoodCategoryCreate, FoodCategoryUpdate]
crud_food_category = CRUDFoodCategory(FoodCategory)
