import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # This will download and manage the correct ChromeDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://localhost:3000")
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("password")
    driver.find_element("tag name", "button").click()
    time.sleep(1)
    assert "Todo List" in driver.page_source

def test_invalid_login(driver):
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("wrong")
    driver.find_element("tag name", "button").click()
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        assert alert.text == "Invalid credentials"
        alert.accept()
    except NoAlertPresentException:
        pytest.fail("Expected alert for invalid login but none was found")
