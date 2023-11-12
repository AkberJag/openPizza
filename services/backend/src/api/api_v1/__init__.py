"""API v1 module"""

from fastapi import APIRouter

from src.config import settings
from .endpoints import auth, food, order

api_v1_router = APIRouter(prefix=settings.API_V1_URL)

api_v1_router.include_router(auth.router, tags=["Auth"])
api_v1_router.include_router(
    food.router, tags=["Food Categories and Items"], prefix="/home"
)
api_v1_router.include_router(order.router, tags=["Orders"], prefix="/order")
