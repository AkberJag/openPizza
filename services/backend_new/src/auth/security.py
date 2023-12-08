"""Security utilities."""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare a plain password with its hashed counterpart to determine if they match."""

    return pwd_context.verify(plain_password, hashed_password)


def generate_password_hash(password: str) -> str:
    """Generates a hash of the provided plain text password using a secure hashing algorithm."""

    return pwd_context.hash(password)
