"""Main application package containing the app factory function."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import api_v1


def create_application() -> FastAPI:
    """Create application factory"""
    application = FastAPI()
    include_routers(application)
    include_middleware(application)
    return application


def include_routers(application: FastAPI) -> None:
    """Include FastAPI routers."""
    application.include_router(api_v1.api_v1_router)


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
