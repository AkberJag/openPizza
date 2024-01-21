from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.auth.dependencies import get_current_active_user
from src.utils.db import get_db

from . import schemas, services
from .constants import metadata_info_register

router = APIRouter(prefix="/user", tags=["User"])


@router.post(
    "/",
    **metadata_info_register,
    status_code=status.HTTP_200_OK,
    response_model=schemas.User,
)
async def user_registration(
    user_in: schemas.UserCreate, db: Annotated[Session, Depends(get_db)]
):
    """Create new user"""

    return await services.register_new_user(db, user_in=user_in)


@router.get(
    "/logout",
    status_code=status.HTTP_200_OK,
)
async def logout(user: Annotated[schemas.User, Depends(get_current_active_user)]):
    content = {
        "message": "You've successfully logged out",
    }
    response = JSONResponse(content=content)
    response.delete_cookie("access_token")
    return response


@router.get("/me", response_model=schemas.UserInDB)
def me(user: Annotated[schemas.User, Depends(get_current_active_user)]):
    """Return logged in user's details"""
    return user
