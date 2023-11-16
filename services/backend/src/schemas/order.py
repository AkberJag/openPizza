"""Order schemas"""

from datetime import datetime

from pydantic import BaseModel
from .order_item import OrderItem


class OrderBase(BaseModel):
    """shared properties"""

    tax_val: None | float = None
    order_notes: None | str = None


class OrderCreate(OrderBase):
    """Properties to receive via API on creation"""

    order_items: list[OrderItem]


class OrderUpdate(OrderBase):
    """Properties to receive via API on update"""


class OrderInDBBase(OrderBase):
    """Shared properties - db"""

    order_id: int

    class Config:
        from_attributes = True


class OrderCategory(OrderInDBBase):
    """Additional properties to return via API"""


class OrderInDB(OrderInDBBase):
    """Additional properties stored in DB"""

    created_at: datetime
