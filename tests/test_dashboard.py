def test_dashboard_load(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title