from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.auth.dependencies import get_current_user
from src.crud.food import crud_food_category
from src.schemas.food import FoodCategory as FoodCategory_schema

router = APIRouter()


@router.get(
    "/food_categories",
    dependencies=[Depends(get_current_user)],
    response_model=list[FoodCategory_schema],
)
async def food_categories(db: Session = Depends(get_db)):
    return crud_food_category.get_multi(db)
