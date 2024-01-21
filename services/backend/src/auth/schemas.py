from pydantic import BaseModel


class LoginReturn(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool


class TokenData(BaseModel):
    email: None | str = None
