"""Order services"""

from . import models
from .crud import crud_order
from .exceptions import OrderNotFound


async def place_new_order(db, *, items_in, user_id: int) -> models.Order:
    """Place new order details in db"""

    return await crud_order.create(db, obj_in=items_in, owner_id=user_id)


def get_order_details(db, *, order_id: int) -> models.Order:
    """Return order detail by id from db"""

    order = crud_order.get(db, id=order_id)

    if not order:
        raise OrderNotFound()

    return order


def get_all_orders(db) -> list[models.Order]:
    """Get all orders from db"""
    return crud_order.get_multi(db)
