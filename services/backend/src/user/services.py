from sqlalchemy.exc import IntegrityError

from . import models
from .crud import crud_user
from .exceptions import EmailTaken


async def register_new_user(db, *, user_in) -> models.User:
    """Register new user service"""
    try:
        return crud_user.create(db, obj_in=user_in)

    except IntegrityError as exc:
        raise EmailTaken from exc


async def get_current_user_details(db, *, email: str) -> models.User:
    """Returen current logged in user details"""

    return crud_user.get_by_email(db, email=email)
