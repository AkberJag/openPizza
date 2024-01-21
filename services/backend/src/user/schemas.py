"""User schemas."""

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """shared properties"""

    name: None | str = None
    email: None | EmailStr = None


class UserCreate(UserBase):
    """Properties to receive via API on creation"""

    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    """Properties to receive via API on update"""


class User(UserBase):
    """Additional properties to return via API"""


class UserInDB(UserBase):
    """Additional properties stored in DB"""

    is_active: bool = True
    is_superuser: bool = False

    id: int
