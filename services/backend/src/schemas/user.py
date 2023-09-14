"""User schemas"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Shared properties"""

    fullname: None | str = None
    email: None | EmailStr = None
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    """Properties to receive via API on creation"""

    fullname: str
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """Properties to receive via API on update"""

    password: None | str = None
