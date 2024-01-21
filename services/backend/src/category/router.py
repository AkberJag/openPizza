from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.orm import Session
from src.utils.db import get_db

from . import schemas, services
from .constants import (
    metadata_info_create_category,
    metadata_info_get_all_categories,
    metadata_info_get_category,
)

router = APIRouter(prefix="/category", tags=["Category"])


@router.post(
    "/",
    **metadata_info_create_category,
    response_model=schemas.Category,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    category_in: schemas.CategoryCreate,
    db: Session = Depends(get_db),
):
    """Create food category"""

    return await services.create_food_category(db, category_in=category_in)


@router.get(
    "/all", **metadata_info_get_all_categories, response_model=list[schemas.Category]
)
async def get_all_categories(db: Session = Depends(get_db)):
    """Create food category"""

    return await services.get_all_categories(db)


@router.get(
    "/{category_id}",
    **metadata_info_get_category,
    response_model=schemas.CategoryWithItems,
)
async def get_category(
    category_id: Annotated[int, Path()], db: Session = Depends(get_db)
):
    """Get a category with all its items"""

    return await services.get_food_category(db, category_id=category_id)
