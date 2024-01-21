"""User specific crud opertations"""


from sqlalchemy.orm import Session
from src.auth.security import verify_password
from src.utils.curd_base import CRUDBase

from .exceptions import InvalidCredentials
from .models import User
from .schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    """User specific crud opertations"""

    def get_by_email(self, db: Session, *, email: str) -> User | None:
        """Return a user object by email adderss"""
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, *, email: str, password: str) -> User | None:
        """Authenticate a user if the provided password is correct"""
        user = self.get_by_email(db, email=email)
        if not user:
            raise InvalidCredentials()
        if not verify_password(password, user.password):
            raise InvalidCredentials()
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


crud_user = CRUDUser(User)
