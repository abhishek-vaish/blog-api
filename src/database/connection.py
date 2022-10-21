from tortoise import Tortoise

from config import settings


TORTOISE_ORM = {
    "connections": {"default": f"{settings.db_url}"},
    "apps": {
        "models": {
            "models": ["app.user.models", "app.blog.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def connect_db():
    """Connect Database"""
    await Tortoise.init(
        db_url=f"{settings.db_url}",
        modules={"models": ["app.user.models", "app.blog.models", "aerich.models"]},
    )
