from fastapi import Depends
from fastapi.security import APIKeyHeader
from pathlib import Path
from passlib.context import CryptContext
from pydantic import ValidationError

from app.user.models import TokenTortoise
from app.user.schema import TokenSchema


BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

apiHeader = APIKeyHeader(name="Token")
context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Convert plain text to hash value"""

    return context.hash(plain_password)


def verify_password(password: str, hash_password: str) -> bool:
    """Verify is hash value is the possible case for the plain text"""

    return context.verify(password, hash_password)


async def verify_token(user_token: TokenSchema = Depends(apiHeader)) -> any:
    """Verify token present in the database for the user or not and returns the user"""

    try:
        user = await TokenTortoise.filter(token=user_token).first()
        if user:
            return user.user_id
        return None
    except ValidationError as e:
        return e
