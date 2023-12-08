from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from src.utils.db import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    items = relationship("Item", back_populates="category")

    @validates("name")
    def convert_upper(self, _key, value: str):
        return value.title()
