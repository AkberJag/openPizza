from datetime import datetime
from pydantic import BaseModel


class FoodCategoryBase(BaseModel):
    """shared properties"""

    category_name: None | str = None


class FoodCategoryCreate(FoodCategoryBase):
    """Properties to receive via API on creation"""

    category_name: str


class FoodCategoryUpdate(FoodCategoryBase):
    """Properties to receive via API on update"""


class FoodCategoryInDBBase(BaseModel):
    """Shared properties - db"""

    category_name: str

    class Config:
        from_attributes = True


class FoodCategory(FoodCategoryInDBBase):
    """Additional properties to return via API"""

    category_id: int


class FoodCategoryInDB(FoodCategoryInDBBase):
    """Additional properties stored in DB"""

    created_at: datetime
