from pydantic import BaseModel
from typing import Optional


class BlogSchema(BaseModel):
    title: str
    description: str


class BlogDbSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True


class UpdateBlogSchema(BlogSchema):
    title: Optional[str]
    description: Optional[str]


class DeleteBlogSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True
