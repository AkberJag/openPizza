import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Config(BaseModel):
    """App settings"""

    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        "postgresql://hello_fastapi:hello_fastapi@localhost/hello_fastapi_dev",
    )


settings = Config()
