"""Local Auth config"""

import os

from pydantic import BaseModel


class AuthConfig(BaseModel):
    """Auth config"""

    JWT_ALG: str = "HS256"
    JWT_SECRET: str = os.getenv("JWT_SECRET_KEY", "SuperSecretKey")
    # 60 minutes * 24 hours * 8 days = 8 days in minutes
    JWT_EXP: int = 60 * 24 * 8


auth_config = AuthConfig()
