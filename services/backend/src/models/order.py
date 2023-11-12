"""Order and item models"""

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
)

from .base import Base


class Order(Base):
    """Order model"""

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tax_val = Column(Integer, default=0)
    tax_enabled = Column(Boolean, default=False)
    order_notes = Column(Text)

    order_items = relationship("OrderItems", back_populates="order")


class OrderItems(Base):
    """Order items model"""

    __tablename__ = "order_items"

    item_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("food_items.item_id"), index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer, index=True)
    price_per_unit = Column(Float)

    order_id = Column(Integer, ForeignKey("orders.order_id"))

    item_notes = Column(Text)

    order = relationship("Order", back_populates="order_items")
