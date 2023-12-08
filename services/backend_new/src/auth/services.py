"""Auth related services."""

from src.user.crud import crud_user


def authenticate_user(db, auth_data):
    """Verify a uses auth data"""
    return crud_user.authenticate(
        db, email=auth_data.username, password=auth_data.password
    )
