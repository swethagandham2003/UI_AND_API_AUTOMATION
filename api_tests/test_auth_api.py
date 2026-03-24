from services.auth_service import AuthService


def test_valid_login():

    auth = AuthService()
    res = auth.login("test@test.com", "123")

    assert res.status_code == 200