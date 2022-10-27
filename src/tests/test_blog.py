import pytest
from fastapi import status
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_create_blog(user_login, client: AsyncClient):
    payload = {"title": "Test Blog", "description": "Test Description"}

    response = await client.post(
        app.url_path_for("blog:create"), json=payload, headers=user_login
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_delete_blog(user_login, blog_create, client: AsyncClient):
    response = await client.delete(
        app.url_path_for("blog:delete", id=blog_create["id"]), headers=user_login
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.anyio
async def test_update_blog(user_login, blog_create, client: AsyncClient):
    payload = {"title": "Update Title"}
    response = await client.patch(
        app.url_path_for("blog:update", id=blog_create["id"]),
        json=payload,
        headers=user_login,
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_user_blog(user_login, client: AsyncClient):
    response = await client.get(app.url_path_for("blog:user"), headers=user_login)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_all_blog(client: AsyncClient):
    response = await client.get(app.url_path_for("blog:default"))
    assert response.status_code == status.HTTP_200_OK