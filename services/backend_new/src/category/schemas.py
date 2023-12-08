from pydantic import BaseModel
from src.item.schemas import Item


class CategoryBase(BaseModel):
    """shared properties"""

    name: None | str = None


class CategoryCreate(CategoryBase):
    """Properties to receive via API on creation"""

    name: str


class CategoryUpdate(CategoryBase):
    """Properties to receive via API on update"""


class CategoryInDBBase(CategoryBase):
    """Shared properties - db"""

    id: int

    class Config:
        from_attributes = True


class Category(CategoryInDBBase):
    """Additional properties to return via API"""


class CategoryWithItems(CategoryInDBBase):
    """Additional properties to return via API"""

    items: list[Item]


class CategoryInDB(CategoryInDBBase):
    """Additional properties stored in DB"""
