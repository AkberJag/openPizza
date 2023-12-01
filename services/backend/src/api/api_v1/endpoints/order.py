from fastapi import APIRouter, Depends, HTTPException, status, Request
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


@router.get("/all")
async def get_all_orders(db: Session = Depends(get_db)):
    return crud_order.get_multi(db)


@router.get("/{order_id}")
async def get_order_items(order_id: int, db: Session = Depends(get_db)):
    return crud_order.get_order_items(db, order_id=order_id)
