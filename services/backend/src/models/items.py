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
