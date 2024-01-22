"""Order schemas"""

from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    """shared properties"""

    name: None | str = None
    quantity: None | int = Field(gt=0)
    price_per_unit: None | float = Field(gt=0)
    item_notes: None | str = None


class OrderItemCreate(OrderItemBase):
    """Properties to receive via API on creation"""

    name: str
    quantity: int
    price_per_unit: float
    item_id: int


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

    id: int
    item_id: int
