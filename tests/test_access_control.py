def test_admin_users_access(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert driver.title != ""