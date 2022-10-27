from fastapi import status
import pytest
from httpx import AsyncClient
from tortoise import Tortoise

from config import settings
from main import app

DB_URL = settings.db_url


async def init_db(db_url, create_db: bool = False, schemas: bool = False) -> None:
    """Initial database connection"""

    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["app.user.models", "app.blog.models"]},
        _create_db=create_db,
    )
    if schemas:
        await Tortoise.generate_schemas()


async def init(db_url: str = DB_URL):
    await init_db(db_url, True, True)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await init()
    yield
    await Tortoise._drop_databases()


@pytest.fixture(scope="session")
async def user_registration(client: AsyncClient):
    payload = {
        "username": "tester",
        "first_name": "test",
        "last_name": "user",
        "password": "12345678",
        "email": "tester@gmail.com",
    }
    response = await client.post(app.url_path_for("auth:register"), json=payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture(scope="session")
async def user_login(user_registration, client: AsyncClient):
    payload = {"username": "tester", "password": "12345678"}

    response = await client.post(app.url_path_for("auth:login"), json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    yield response.json()


@pytest.fixture(scope="session")
async def blog_create(user_login, client: AsyncClient):
    payload = {"title": "Test Blog", "description": "Test Description"}
    response = await client.post(
        app.url_path_for("blog:create"), json=payload, headers=user_login
    )
    assert response.status_code == status.HTTP_201_CREATED
    yield response.json()
