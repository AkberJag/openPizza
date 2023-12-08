import os
from typing import Any

from pydantic import BaseModel
from src.utils.constants import Environment, api_metadata

APP_ENV = os.getenv("APP_ENV", "development")


class Config(BaseModel):
    """App settings"""

    APP_TITLE: str = "openPizza"
    APP_VERSION: str = "0.0.1"

    ENVIRONMENT: Environment = Environment.TESTING

    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:password@localhost:5432/ecommerce",
    )
    API_V1_URL: str = "/api/v1"


settings = Config()

app_configs: dict[str, Any] = dict()
app_configs["title"] = settings.APP_TITLE + "🍕"
app_configs["version"] = settings.APP_VERSION
app_configs.update(api_metadata)


if not settings.ENVIRONMENT.is_debug:
    app_configs["openapi_url"] = None  # hide docs
