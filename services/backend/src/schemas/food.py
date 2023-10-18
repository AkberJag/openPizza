from datetime import datetime
from pydantic import BaseModel, HttpUrl


# Food Category
class FoodCategoryBase(BaseModel):
    """shared properties"""

    category_name: None | str = None


class FoodCategoryCreate(FoodCategoryBase):
    """Properties to receive via API on creation"""

    category_name: str


class FoodCategoryUpdate(FoodCategoryBase):
    """Properties to receive via API on update"""


class FoodCategoryInDBBase(FoodCategoryBase):
    """Shared properties - db"""

    category_id: int

    class Config:
        from_attributes = True


class FoodCategory(FoodCategoryInDBBase):
    """Additional properties to return via API"""


class FoodCategoryInDB(FoodCategoryInDBBase):
    """Additional properties stored in DB"""

    created_at: datetime
