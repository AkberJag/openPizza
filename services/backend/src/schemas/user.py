"""User schemas"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """shared properties"""

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


class UserInDBBase(UserBase):
    """Shared properties - db"""

    id: None | int = None

    class Config:
        from_attributes = True


class User(UserInDBBase):
    """Additional properties to return via API"""


class UserInDB(UserInDBBase):
    """Additional properties stored in DB"""

    hashed_password: str
