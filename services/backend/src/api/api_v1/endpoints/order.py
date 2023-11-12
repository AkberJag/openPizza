from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.database.session import get_db
from src.auth.dependencies import get_current_user
from src.crud.food import crud_food_category, crud_food_item
from src.schemas.food import FoodCategory as FoodCategory_schema
from src.schemas.food import FoodCategoryCreate, FoodItem, FoodItemCreate
from src.schemas import OrderCreate
from src.crud import crud_order


router = APIRouter()


@router.post("/")
async def make_order(order: OrderCreate, db: Session = Depends(get_db)):
    return crud_order.create_order(db, order=order)
