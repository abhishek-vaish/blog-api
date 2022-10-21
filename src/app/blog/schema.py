from typing import Optional

from pydantic import BaseModel


class BlogSchema(BaseModel):
    """Blog Base Schema"""

    title: str
    description: str


class BlogDbSchema(BaseModel):
    """Blog Database Return Schema"""

    id: int

    class Config:
        orm_mode = True


class UpdateBlogSchema(BlogSchema):
    """Blog Update Schema"""

    title: Optional[str]
    description: Optional[str]


class DeleteBlogSchema(BaseModel):
    """Blog Delete Schema"""

    id: int

    class Config:
        orm_mode = True
