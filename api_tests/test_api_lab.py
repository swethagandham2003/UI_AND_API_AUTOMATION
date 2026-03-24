import pytest
from api_utils.http_client import HttpClient


@pytest.mark.parametrize("endpoint,expected", [
    ("/users", 200),
    ("/posts/1", 200),
    ("/comments", 200)
])
def test_status_codes(endpoint, expected):

    client = HttpClient()
    response = client.get(endpoint)

    assert response.status_code == expected