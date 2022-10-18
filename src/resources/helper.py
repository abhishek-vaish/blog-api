from configparser import ConfigParser
from pathlib import Path
import os

from fastapi import Depends
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext
from pydantic import ValidationError

from app.user.models import TokenTortoise
from app.user.schema import TokenSchema

apiHeader = APIKeyHeader(name="Token")

BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

ENV = os.environ.setdefault("BLOG_ENV", "development")

parser = ConfigParser()
parser.read(RESOURCES_DIR / f"{ENV}.ini")

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    return context.hash(plain_password)


def verify_password(password: str, hash_password: str) -> bool:
    return context.verify(password, hash_password)


async def verify_token(user_token: TokenSchema = Depends(apiHeader)):
    try:
        user = await TokenTortoise.filter(token=user_token).first()
        if user:
            return user.user_id
        return None
    except ValidationError as e:
        return e
