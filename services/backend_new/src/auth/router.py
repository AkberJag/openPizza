from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.utils.db import get_db

from .constants import metadata_info_login
from .jwthandler import create_access_token
from .schemas import LoginReturn
from .services import authenticate_user

router = APIRouter(tags=["Auth"])


@router.post("/login", **metadata_info_login, response_model=LoginReturn)
async def login(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    """User login with Email and Password"""

    user = authenticate_user(db, form_data)

    # Generate a JWT Token
    token = create_access_token(user=user)

    response.set_cookie(
        "access_token",
        value=f"Bearer {token}",
        httponly=True,
        samesite="Lax",
        secure=False,
    )

    return user
