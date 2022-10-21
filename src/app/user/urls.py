from fastapi import APIRouter, status, Depends, HTTPException, Request
from .schema import UserSchema, UserLogin, UpdateUserSchema
from .crud import db_register, db_login, db_logout, db_get_user, db_user_update
from resources.helper import verify_token

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, name="auth:register")
async def register(user: UserSchema):
    """URL: User Registration"""

    return await db_register(user)


@router.post("/login", status_code=status.HTTP_201_CREATED, name="auth:login")
async def login(user: UserLogin):
    """URL: User Login"""

    return await db_login(user)


@router.delete("/logout", status_code=status.HTTP_204_NO_CONTENT, name="auth:logout")
async def logout(request: Request, user_id: int = Depends(verify_token)):
    """URL: User Logout"""

    if user_id:
        print(request)
        return await db_logout(user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.patch("/update", status_code=status.HTTP_200_OK, name="auth:update")
async def update_user(user: UpdateUserSchema, user_id: int = Depends(verify_token)):
    """URL: Update User Information"""

    if user_id:
        return await db_user_update(user, user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/get-user", status_code=status.HTTP_200_OK, name="auth:default")
async def get_user(user_id: int = Depends(verify_token)):
    """URL: Get Current Login User"""

    if user_id:
        return await db_get_user(user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
