from src.utils.curd_base import CRUDBase

from .models import OrderItem
from .schemas import OrderItemCreate, OrderItemUpdate

CRUDOrderItem = CRUDBase[OrderItem, OrderItemCreate, OrderItemUpdate]


crud_order_item = CRUDOrderItem(OrderItem)
