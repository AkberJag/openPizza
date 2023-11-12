"""Order schemas"""

from pydantic import BaseModel

from src.models.order import OrderItems


class OrderItemBase(BaseModel):
    """shared properties"""

    product_id: None | int = None
    quantity: None | int = None
    price_per_unit: None | int = None
    item_notes: None | str = None
    product_name: None | str = None

    class Meta:
        orm_model = OrderItems


class OrderItemCreate(OrderItemBase):
    """Properties to receive via API on creation"""

    product_id: int
    quantity: int
    price_per_unit: int
    product_name: str


class OrderItemUpdate(OrderItemBase):
    """Properties to receive via API on update"""


class OrderItemInDBBase(OrderItemBase):
    """Shared properties - db"""

    class Config:
        from_attributes = True


class OrderItem(OrderItemInDBBase):
    """Additional properties to return via API"""


class OrderItemInDB(OrderItemInDBBase):
    """Additional properties stored in DB"""

    item_id: int
