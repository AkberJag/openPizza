from typing import Annotated

from fastapi import Depends
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from src.user.crud import crud_user
from src.user.schemas import User
from src.utils.db import get_db

from .config import auth_config
from .exceptions import (
    InvalidCredentials,
    InvalidInput,
    InvalidToken,
    UserInactive,
    UserNotFound,
)
from .jwthandler import oauth2_scheme


def get_current_user(
    access_token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(
            access_token, auth_config.JWT_SECRET, algorithms=[auth_config.JWT_ALG]
        )

        userid: str | None = payload.get("sub")
        if userid is None:
            raise InvalidCredentials()
    except JWTError as exc:
        raise InvalidToken() from exc
    except ValidationError as exc:
        raise InvalidInput() from exc

    user = crud_user.get(db, id=userid)

    if not user:
        raise UserNotFound()

    return user


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    if not current_user.is_active:
        raise UserInactive()
    return current_user
