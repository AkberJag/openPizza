from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.router import router as auth_router
from src.category.router import router as category_router
from src.item.router import router as item_router
from src.orders.router import router as order_router
from src.user.router import router as user_router

from .config import app_configs
from .utils.constants import tags_metadata


def create_application() -> FastAPI:
    """Create application factory"""
    application = FastAPI(**app_configs, openapi_tags=tags_metadata)
    include_routers(application)
    include_middleware(application)
    return application


def include_routers(application: FastAPI) -> None:
    """Include FastAPI routers."""
    application.include_router(auth_router)
    application.include_router(user_router)
    application.include_router(item_router)
    application.include_router(category_router)
    application.include_router(order_router)


def include_middleware(application: FastAPI) -> None:
    """Include Middlewares"""
    origins = ["http://localhost:8080"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app = create_application()
