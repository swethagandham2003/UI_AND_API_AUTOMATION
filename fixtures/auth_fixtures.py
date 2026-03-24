import pytest
from services.auth_service import AuthService


@pytest.fixture
def auth_token():

    auth = AuthService()

    response = auth.login("eve.holt@reqres.in", "cityslicka")

    return response.json()["token"]