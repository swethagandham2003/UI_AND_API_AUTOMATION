from services.user_service import UserService


def test_get_users():

    user = UserService()
    res = user.get_users()

    assert res.status_code == 200


def test_create_user():

    user = UserService()
    res = user.create_user("Rupa", "QA")

    assert res.status_code == 201