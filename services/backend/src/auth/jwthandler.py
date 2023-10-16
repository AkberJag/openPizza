"""JSON Web Token (JWT) Handling Module"""

from typing import Any
from datetime import timedelta, datetime

from fastapi import HTTPException, Request
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt

from src.config import settings
from src.auth.config import auth_config


class OAuth2PasswordBearerCookie(OAuth2):
    # this is a slightly modified version of 'OAuth2PasswordBearer'
    # refer to the fastAPI issue #480
    def __init__(
        self,
        token_url: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": token_url, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> str | None:
        authorization: str = request.cookies.get("access_token")
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None

        return param


security = OAuth2PasswordBearerCookie(token_url=settings.API_V1_URL + "/login")


def create_access_token(
    *,
    user,
    expires_delta: timedelta = timedelta(minutes=auth_config.JWT_EXP),
) -> str:
    """Create the jwt token for a user

    Returns:
        str: JWT encoded string
    """
    jwt_data = {
        "sub": str(user.id),
        "exp": datetime.utcnow() + expires_delta,
        # "is_admin": user["is_admin"], -> for future when RBAC is added to the project
    }

    return jwt.encode(jwt_data, auth_config.JWT_SECRET, algorithm=auth_config.JWT_ALG)
