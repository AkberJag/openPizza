from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from src.utils.db import Base


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, default=0)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="items")
    order_items = relationship("OrderItem", back_populates="item")

    @validates("name")
    def convert_upper(self, _key, value: str):
        return value.title()

    # getting a weird error so this is a quick fix for that :')
    # "can't adapt type 'pydantic_core._pydantic_core.Url'"
    @validates("image_url")
    def url_to_str(self, _key, value: str):
        return str(value) if value else None
