"""User specific crud opertations"""

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .base import CRUDBase
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.auth.security import verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """User specific crud opertations"""

    def get_by_email(self, db: Session, *, email: str) -> User | None:
        """Return a user object by email adderss"""
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, *, email: str, password: str) -> User | None:
        """Authenticate a user if the provided password is correct"""
        user = self.get_by_email(db, email=email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
            )
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


crud_user = CRUDUser(User)
