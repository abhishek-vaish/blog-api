from fastapi import APIRouter, status, Depends, HTTPException, Request
from .schema import UserSchema, UserLogin, UpdateUserSchema
from .crud import db_register, db_login, db_logout, db_get_user, db_user_update
from resources.helper import verify_token

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserSchema):
    return await db_register(user)


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: UserLogin):
    return await db_login(user)


@router.delete("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(request: Request, user_id: int = Depends(verify_token)):
    if user_id:
        print(request)
        return await db_logout(user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.patch("/update", status_code=status.HTTP_200_OK)
async def update_user(user: UpdateUserSchema, user_id: int = Depends(verify_token)):
    if user_id:
        return await db_user_update(user, user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user_id: int = Depends(verify_token)):
    if user_id:
        return await db_get_user(user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
