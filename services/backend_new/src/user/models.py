"""User model"""

from sqlalchemy import Boolean, Column, DateTime, Integer, String, event
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from src.auth import security
from src.utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    order = relationship("Order", back_populates="user_info", foreign_keys="Order.user")
    created_orders = relationship(
        "Order", back_populates="order_owner_info", foreign_keys="Order.order_owner"
    )

    # Event listener for hashing password before saving to the database
    @staticmethod
    def _hash_password(_mapper, _connection, target):
        if target.password:
            target.password = security.generate_password_hash(target.password)

    @validates("name")
    def convert_upper(self, _key, value: str):
        return value.title()


# Attaching the listener to the User model
event.listen(User, "before_insert", User._hash_password)
event.listen(User, "before_update", User._hash_password)
