""" A lazy way of importing required models and exposing them to 
    the alembic env.py insted of adding all models directly to the 
    env.py file
    suggest me a better way please 🥺
"""

from src.category.models import Category  # noqa: F401
from src.item.models import Item  # noqa: F401
from src.orders.order.models import Order  # noqa: F401
from src.orders.order_items.models import OrderItem  # noqa: F401
from src.user.models import User  # noqa: F401
