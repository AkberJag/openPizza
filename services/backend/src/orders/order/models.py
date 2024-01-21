from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.utils.db import Base


class Order(Base):
    """Order model"""

    __tablename__ = "order"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    tax_val = Column(Integer, default=0)
    order_notes = Column(Text)
    order_total = Column(Float)
    delivery_charge = Column(Float)
    extra_charge_reason = Column(Text)
    extra_charge = Column(Float)
    order_type = Column(String)

    user = Column(Integer, ForeignKey("users.id"))
    order_owner = Column(Integer, ForeignKey("users.id"))

    user_info = relationship("User", back_populates="order", foreign_keys=[user])
    order_owner_info = relationship(
        "User", back_populates="order", foreign_keys=[order_owner]
    )

    order_items = relationship("OrderItem", back_populates="order")
