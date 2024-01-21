"""Order schemas"""

from datetime import datetime

from pydantic import BaseModel, Field
from src.orders.order_items.schemas import OrderItemCreate, OrderItemInDB


class OrderBase(BaseModel):
    """shared properties"""

    tax_val: None | float = None
    order_notes: None | str = None


class OrderCreate(OrderBase):
    """Properties to receive via API on creation"""

    order_type: str
    extra_charge: float
    extra_charge_reason: str
    delivery_charge: float
    order_items: list[OrderItemCreate]
    user: int = Field(alias="customer")


class OrderUpdate(OrderBase):
    """Properties to receive via API on update"""


class OrderInDBBase(OrderBase):
    """Shared properties - db"""

    id: int
    user: int
    created_at: datetime
    order_owner: int
    order_total: float
    extra_charge_reason: str
    extra_charge: float
    order_type: str

    class Config:
        from_attributes = True


class Order(OrderInDBBase):
    """Additional properties to return via API"""


class OrderInDB(OrderInDBBase):
    """Additional properties stored in DB"""

    order_items: list[OrderItemInDB]
