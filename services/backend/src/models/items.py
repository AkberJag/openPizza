"""Food models"""

from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from .base import Base


class FoodCategories(Base):
    """Food category model"""

    __tabelname__ = "food_categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Define a relationship to FoodItem
    items = relationship("FoodItem", back_populates="category")


class FoodItems(Base):
    """Food items model"""

    __tablename__ = "food_items"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("food_categories.category_id"))
    price = Column(Float)

    image_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationship to FoodCategory
    category = relationship("FoodCategory", back_populates="items")
