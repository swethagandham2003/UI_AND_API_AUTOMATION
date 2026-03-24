def assert_status(response, expected):
    assert response.status_code == expected


def assert_key(data, key):
    assert key in data