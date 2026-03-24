def test_alerts(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    assert "JavaScript Alerts" in driver.page_source