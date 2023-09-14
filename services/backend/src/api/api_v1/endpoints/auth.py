"""auth routes"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.crud import crud_user
from src.schemas import UserCreate, UserInDB
from src.database.session import get_db
from src.auth.security import get_password_hash

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
