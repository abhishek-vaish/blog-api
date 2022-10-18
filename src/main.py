from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

from app.user.urls import router as user_router
from app.blog.urls import router as blog_router
from database.connection import connect_db, TORTOISE_ORM

app = FastAPI()

register_tortoise(app, TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True)


@app.on_event("startup")
async def startup():
    await connect_db()
    await Tortoise.generate_schemas()


app.include_router(user_router, prefix="/api/v1/user")
app.include_router(blog_router, prefix="/api/v1/blog")


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)
