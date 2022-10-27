import pytest
from fastapi import status
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_user_registration(client: AsyncClient):
    payload = {
        "username": "new_tester",
        "first_name": "test",
        "last_name": "user",
        "password": "12345678",
        "email": "tester@gmail.com",
    }

    response = await client.post(app.url_path_for("auth:register"), json=payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.fixture(scope="session")
async def test_user_login(client: AsyncClient):
    payload = {"username": "new_tester", "password": "12345678"}

    response = await client.post(app.url_path_for("auth:login"), json=payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_user_logout(user_login, client: AsyncClient):
    response = await client.delete(app.url_path_for("auth:logout"), headers=user_login)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.anyio
async def test_get_user(user_login, client: AsyncClient):
    response = await client.get(app.url_path_for("auth:default"), headers=user_login)
    assert response.status_code == status.HTTP_200_OK
