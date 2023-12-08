from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.auth.dependencies import get_current_active_user
from src.utils.db import get_db

from . import schemas, services
from .constants import metadata_info_register

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", **metadata_info_register, status_code=status.HTTP_204_NO_CONTENT)
async def user_registration(
    user_in: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]
):
    """Create new user"""

    await services.register_new_user(db, user_in=user_in)


@router.get("/me", response_model=schemas.UserInDB)
def me(user: Annotated[schemas.User, Depends(get_current_active_user)]):
    """Return logged in user's details"""
    return user
