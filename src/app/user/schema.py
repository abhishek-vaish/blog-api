from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    """User Main Schema"""

    username: str
    first_name: str
    last_name: Optional[str]
    email: Optional[EmailStr]
    password: str

    class Config:
        orm_mode = True


class UserDBSchema(UserSchema):
    """User Schema to return id"""

    id: int


class UserLogin(BaseModel):
    """User Schema required at time of login"""

    username: str
    password: str

    class Config:
        orm_mode = True


class UpdateUserSchema(UserSchema):
    """User schema required while updating user details"""

    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]


class TokenSchema(BaseModel):
    """Token Schema for token validation"""

    token: str
