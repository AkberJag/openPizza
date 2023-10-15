"""Food models"""

from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from .base import Base


class FoodCategory(Base):
    """Food category model"""

    __tablename__ = "food_categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to FoodItem
    food_items = relationship("FoodItem", back_populates="food_category")


class FoodItem(Base):
    """Food items model"""

    __tablename__ = "food_items"

    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("food_categories.category_id"))
    price = Column(Float)
    image_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to FoodCategory
    food_category = relationship("FoodCategory", back_populates="food_items")
