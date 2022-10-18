from tortoise import Tortoise
from resources.helper import parser

TORTOISE_ORM = {
    "connections": {"default": "sqlite://sqlite.dev.db"},
    "apps": {
        "models": {
            "models": ["app.user.models", "app.blog.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}


async def connect_db():
    await Tortoise.init(
        db_url=parser["DEFAULT"]["DB_URL"],
        modules={"models": ["app.user.models", "app.blog.models", "aerich.models"]},
    )
