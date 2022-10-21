import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app=app)


def test_user_registration():
    # payload = {
    #     "username": "tester",
    #     "first_name": "test",
    #     "last_name": "user",
    #     "password": "12345678",
    #     "email": "tester@gmail.com",
    # }
    response = client.get(app.url_path_for("/"))
    assert response.status_code == status.HTTP_200_OK

    # def test_user_login():
    #     payload = {
    #         "username": "tester",
    #         "password": "12345678"
    #     }
    #
    #     with TestClient(app) as client:
    #         response = client.post(app.url_path_for("auth:login"), json=payload)
    #         assert response.status_code == status.HTTP_201_CREATED
