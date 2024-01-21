from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.utils.db import Base


class OrderItem(Base):
    """Order items model"""

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    price_per_unit = Column(Float)
    item_notes = Column(String)

    order_id = Column(Integer, ForeignKey("order.id"))
    item_id = Column(Integer, ForeignKey("item.id"))

    order = relationship("Order", back_populates="order_items")
    item = relationship("Item", back_populates="order_items")
