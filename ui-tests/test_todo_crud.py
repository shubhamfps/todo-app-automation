import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")

    # Perform login
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.find_element(By.TAG_NAME, "button").click()

    # Handle possible alert after login
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Alert found: {alert.text}")
        alert.accept()
        pytest.fail(f"Login failed: {alert.text}")
    except NoAlertPresentException:
        pass
    except Exception:
        pass  # Allow test to continue if no alert shows

    # Wait for home page to load after login
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "newTodo")))

    yield driver
    driver.quit()

def test_add_todo(driver):
    driver.find_element(By.NAME, "newTodo").send_keys("Buy Milk")
    driver.find_element(By.ID, "addTodo").click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Buy Milk")
    )
    assert "Buy Milk" in driver.page_source

def test_edit_todo(driver):
    wait = WebDriverWait(driver, 10)

    # Click the edit button
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "edit-btn"))).click()

    # Wait until the editable input appears
    input_box = wait.until(EC.presence_of_element_located((By.NAME, "editTodo")))

    # Clear and enter new text
    input_box.clear()
    input_box.send_keys("Buy Bread")

    # Click the Save button (important!)
    wait.until(EC.element_to_be_clickable((By.ID, "saveTodo"))).click()

    # Wait until the new text is visible
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Buy Bread"))
    assert "Buy Bread" in driver.page_source

def test_delete_todo(driver):
    wait = WebDriverWait(driver, 10)
    # Click the delete button
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "delete-btn"))).click()

    # Wait until the todo is removed from page
    wait.until_not(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Buy Bread"))
    assert "Buy Bread" not in driver.page_source
