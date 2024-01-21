from datetime import datetime

from pydantic import BaseModel, HttpUrl


class ItemBase(BaseModel):
    """shared properties"""

    name: None | str = None
    price: None | float = None
    image_url: None | HttpUrl = None
    description: None | str = None


class ItemCreate(ItemBase):
    """Properties to receive via API on creation"""

    name: str
    price: float
    category_id: int


class ItemUpdate(ItemBase):
    """Properties to receive via API on update"""


class ItemInDBBase(ItemBase):
    """Shared properties - db"""

    id: int

    class Config:
        from_attributes = True


class Item(ItemInDBBase):
    """Additional properties to return via API"""


class ItemInDB(ItemInDBBase):
    """Additional properties stored in DB"""

    created_at: datetime
