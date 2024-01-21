from sqlalchemy.orm import Session
from src.item.crud import crud_item
from src.orders.order_items.models import OrderItem
from src.utils.curd_base import CRUDBase

from .exceptions import ItemNotFound
from .models import Order
from .schemas import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    async def create(self, db: Session, *, obj_in: OrderCreate, owner_id: int) -> Order:
        order_total = 0
        tax_val = obj_in.tax_val or 0

        new_order = Order(
            tax_val=tax_val,
            order_notes=obj_in.order_notes,
            order_owner=owner_id,
            delivery_charge=obj_in.delivery_charge,
            extra_charge_reason=obj_in.extra_charge_reason,
            extra_charge=obj_in.extra_charge,
            order_type=obj_in.order_type,
            user=obj_in.user,
        )

        for item in obj_in.order_items:
            db_item = crud_item.get(db, item.item_id)
            if not db_item:
                raise ItemNotFound(item.name)

            price_for_one = item.price_per_unit + (tax_val * item.price_per_unit)

            order_total += price_for_one * item.quantity
            order_item = OrderItem(
                name=db_item.name,
                quantity=item.quantity,
                price_per_unit=item.price_per_unit,
                item_notes=item.item_notes,
                item_id=db_item.id,
            )

            new_order.order_items.append(order_item)
        new_order.order_total = order_total
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order


crud_order = CRUDOrder(Order)
