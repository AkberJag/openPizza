from typing import Annotated

from fastapi import APIRouter, Depends

from src.models import User
from src.auth.dependencies import get_current_user

router = APIRouter()


@router.get("/")
async def home(current_user: Annotated[User, Depends(get_current_user)]):
    return f"You have access {current_user}"
