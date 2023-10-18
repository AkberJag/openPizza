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


# Food Items
class FoodItemBase(BaseModel):
    """shared properties"""

    item_name: None | str = None
    price: None | float = None
    image_url: None | HttpUrl = None


class FoodItemCreate(FoodItemBase):
    """Properties to receive via API on creation"""

    item_name: str
    price: float

    category_id: int


class FoodItemUpdate(FoodItemBase):
    """Properties to receive via API on update"""


# Food Items - in DB
class FoodItemInDBBase(FoodItemBase):
    """Shared properties - db"""

    item_id: int

    class Config:
        from_attributes = True


class FoodItem(FoodItemInDBBase):
    """Additional properties to return via API"""

    category_id: int


class FoodItemInDB(FoodItemInDBBase):
    """Additional properties stored in DB"""

    created_at: datetime
