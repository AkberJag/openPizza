from src.auth.constants import ErrorCode
from src.utils.exceptions import (
    BadRequest,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
    Unprocessable_Entity,
)


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class InvalidInput(Unprocessable_Entity):
    """"""


class UserNotFound(NotFound):
    DETAIL = ErrorCode.USER_NOT_FOUND


class UserInactive(PermissionDenied):
    DETAIL = ErrorCode.ACCOUNT_DISABLED
