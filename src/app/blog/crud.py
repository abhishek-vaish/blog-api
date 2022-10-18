from pydantic import ValidationError

from app.blog.models import BlogTortoise
from app.blog.schema import BlogSchema, BlogDbSchema, DeleteBlogSchema, UpdateBlogSchema
from app.user.models import UserTortoise


async def db_create_blog(blog: BlogSchema, user_id: int):
    """Create blog in database"""

    blog_body = blog.dict()
    blog_body["user"] = await UserTortoise.filter(id=user_id).first()
    try:
        new_blog = await BlogTortoise.create(**blog_body)
        return BlogDbSchema.from_orm(new_blog)
    except ValidationError as e:
        return e


async def db_read_blog(user_id: int):
    """Read User Created Blog"""

    try:
        return await BlogTortoise.filter(user=user_id).all()
    except ValidationError as e:
        return e


async def db_update_blog(id: int, update_blog: UpdateBlogSchema, user_id: int):
    """Update User Created Blog"""

    try:
        await BlogTortoise.filter(user=user_id, id=id).update(
            **update_blog.dict(exclude_unset=True)
        )
        return {"message": "ok"}
    except ValidationError as e:
        return e


async def db_get_all_blog():
    return await BlogTortoise.all()


async def db_delete_blog(id: int, user_id: int):
    try:
        blog = await BlogTortoise.filter(id=id, user=user_id).delete()
        return DeleteBlogSchema.from_orm(blog)
    except ValidationError as e:
        return e
