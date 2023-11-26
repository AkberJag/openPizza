from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.order import Order, OrderItems
from src.schemas.order import OrderCreate, OrderUpdate


class CRUDFoodItem(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def create_order(self, db: Session, *, order: OrderCreate):
        """Create order and order items"""
        order_data = order.model_dump()

        items_data = order_data.pop("order_items", None)
        db_order_obj = Order(**order_data)

        for item in items_data:
            db_order_item = OrderItems(**item)
            db_order_obj.order_items.append(db_order_item)

        db.add(db_order_obj)
        db.commit()
        db.refresh(db_order_obj)
        return order


crud_order = CRUDFoodItem(Order)
