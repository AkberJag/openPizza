from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from src.orders.order import constants, schemas, services
from src.utils.db import get_db

router = APIRouter(prefix="/order", tags=["Order"])


@router.post(
    "/",
    **constants.metadata_info_place_order,
    response_model=schemas.OrderInDB,
)
async def place_order(
    db: Annotated[Session, Depends(get_db)], items: schemas.OrderCreate
):
    """Create new order"""
    return await services.place_new_order(db, items_in=items, user_id=1)


@router.get(
    "/",
    **constants.metadata_info_get_all_orders,
    response_model=list[schemas.Order],
)
async def get_all_orders(db: Annotated[Session, Depends(get_db)]):
    """Return all orders"""

    return services.get_all_orders(db)


@router.get(
    "/{order_id}",
    **constants.metadata_info_get_order_details,
    # response_model=schemas.OrderInDB,
)
async def get_order_details(
    order_id: Annotated[int, Path(gt=0)],
    db: Annotated[Session, Depends(get_db)],
):
    """Return an order details"""

    return services.get_order_details(db, order_id=order_id)
