from typing import Annotated

from fastapi import Depends, HTTPException, status

from .jwthandler import security


from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from .config import auth_config
from src.database.session import get_db
from src.crud.user import crud_user


def get_current_user(
    access_token: Annotated[str, Depends(security)],
    db: Session = Depends(get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            access_token, auth_config.JWT_SECRET, algorithms=[auth_config.JWT_ALG]
        )

        userid: str | None = payload.get("sub")
        if userid is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    except ValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid input"
        ) from exc

    user = crud_user.get(db, id=userid)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
