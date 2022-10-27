from tortoise import Tortoise

from config import settings


TORTOISE_ORM = {
    "connections": {"default": {
        "engine": "tortoise.backends.asyncpg",
        "credentials": {
            "database": f"{settings.database}",
            "host": f"{settings.host}",
            "password": f"{settings.password}",
            "port": settings.port,
            "user": f"{settings.user}",
        }
    }},
    "apps": {
        "models": {
            "models": ["app.user.models", "app.blog.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def connect_db():
    """Connect Database"""

    await Tortoise.init(TORTOISE_ORM)
