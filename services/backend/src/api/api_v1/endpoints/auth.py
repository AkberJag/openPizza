"""auth routes"""

from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.crud import crud_user
from src.schemas import UserCreate, UserInDB
from src.database.session import get_db
from src.auth.security import get_password_hash
from src.auth.dependencies import get_current_user
from src.models import User
from src.auth.jwthandler import create_access_token

router = APIRouter()


@router.post("/register")
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Create new user"""

    obj_in = UserInDB(
        **user_in.model_dump(), hashed_password=get_password_hash(user_in.password)
    )

    try:
        return crud_user.create(db, obj_in=obj_in)
    except IntegrityError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="This email is already in use"
        ) from exc


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    db_user = crud_user.authenticate(
        db, email=form_data.username, password=form_data.password
    )

    token = create_access_token(user=db_user)

    content = {
        "username": db_user.fullname,
        "message": "You've successfully logged in. Welcome back!",
        "access_token": token,
        "token_type": "bearer",
    }
    response = JSONResponse(content=content)
    response.set_cookie(
        "access_token",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response
