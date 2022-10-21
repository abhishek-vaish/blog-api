from fastapi import HTTPException, status
from pydantic import ValidationError
from uuid import uuid4

from app.user.models import TokenTortoise, UserTortoise
from app.user.schema import UserDBSchema, UserLogin, UserSchema, UpdateUserSchema
from resources.helper import hash_password, verify_password


async def db_register(user: UserSchema):
    """Register new user to the user table"""

    try:
        update_password = user.dict()
        update_password["password"] = hash_password(update_password["password"])
        new_user = await UserTortoise.create(**update_password)
        return UserDBSchema.from_orm(new_user)
    except ValidationError as e:
        return e


async def db_login(user: UserLogin):
    """Login user and create login token to token table"""

    try:
        login_user = await UserTortoise.get(username=user.username)
        if login_user:
            if verify_password(user.password, login_user.password):
                token = {"token": uuid4(), "user": login_user}
                await TokenTortoise.create(**token)
                return {"token": token["token"]}
    except ValidationError as e:
        return e


async def db_logout(user_id: int):
    """Logout current user"""

    try:
        token_delete = await TokenTortoise.filter(user_id=user_id).delete()
        if token_delete:
            return {"status": "delete"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    except ValidationError as e:
        return e


async def db_get_user(user_id: int):
    """Get current login user"""

    try:
        user = await UserTortoise.filter(id=user_id).first()
        return user
    except ValidationError as e:
        return e


async def db_user_update(user: UpdateUserSchema, user_id: int):
    """Update current login user"""

    try:
        await UserTortoise.filter(id=user_id).update(**user.dict(exclude_unset=True))
        return {"message": "ok"}
    except ValidationError as e:
        return e
