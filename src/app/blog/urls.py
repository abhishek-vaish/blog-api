from fastapi import APIRouter, Depends, HTTPException, status
from resources.helper import verify_token

from app.blog.schema import BlogSchema, UpdateBlogSchema
from app.blog.crud import (
    db_create_blog,
    db_delete_blog,
    db_get_all_blog,
    db_read_blog,
    db_update_blog,
)

router = APIRouter()


@router.post("/blog-create", status_code=status.HTTP_201_CREATED, name="blog:create")
async def create_blog(blog: BlogSchema, user_id: int = Depends(verify_token)):
    """URL: Create New Blog"""

    if user_id:
        return await db_create_blog(blog, user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/user-blog", status_code=status.HTTP_200_OK, name="blog:user")
async def get_blog(user_id: int = Depends(verify_token)):
    """URL: Get Current Login User Blog"""

    if user_id:
        return await db_read_blog(user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.patch("/update/{id}", status_code=status.HTTP_200_OK, name="blog:update")
async def update_blog(
    id: int, blog: UpdateBlogSchema, user_id: int = Depends(verify_token)
):
    """URL: Update Blog"""
    if user_id:
        return await db_update_blog(id, blog, user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.delete(
    "/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, name="blog:delete"
)
async def delete_blog(id: int, user_id: int = Depends(verify_token)):
    """URL: Delete Blog"""
    if user_id:
        return await db_delete_blog(id, user_id)
    else:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.get("/", status_code=status.HTTP_200_OK, name="blog:default")
async def get_all_blog():
    """URL: Get All Blog"""
    return await db_get_all_blog()
