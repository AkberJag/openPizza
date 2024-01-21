from src.utils.curd_base import CRUDBase

from .models import Category
from .schemas import CategoryCreate, CategoryUpdate

CRUDCategory = CRUDBase[Category, CategoryCreate, CategoryUpdate]


crud_category = CRUDCategory(Category)
