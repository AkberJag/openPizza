from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.db import get_db

from . import schemas, services
from .constants import metadata_info_create_item

router = APIRouter(prefix="/items", tags=["Item"])


@router.post("/", **metadata_info_create_item, response_model=schemas.Item)
async def create_item(
    item: schemas.ItemCreate, db: Annotated[Session, Depends(get_db)]
):
    """Create a food item"""

    return await services.create_food_item(db, item_in=item)
