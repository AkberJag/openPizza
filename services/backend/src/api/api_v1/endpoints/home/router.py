from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.database.session import get_db
from src.auth.dependencies import get_current_user
from src.crud.food import crud_food_category
from src.schemas.food import FoodCategory as FoodCategory_schema
from src.schemas.food import FoodCategoryCreate

router = APIRouter()


@router.get(
    "/food_categories",
    dependencies=[Depends(get_current_user)],
    response_model=list[FoodCategory_schema],
)
async def food_categories(db: Session = Depends(get_db)):
    return crud_food_category.get_multi(db)


@router.post(
    "/food_category",
    dependencies=[Depends(get_current_user)],
    response_model=FoodCategory_schema,
)
async def add_food_category(
    food_category_in: FoodCategoryCreate, db: Session = Depends(get_db)
):
    try:
        return crud_food_category.create(db, obj_in=food_category_in)
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{food_category_in.category_name} is already exist",
        ) from exc

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}"
        ) from e
