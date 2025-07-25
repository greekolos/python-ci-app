# тестовый случай 1 регистрация и поиск нужного по универсальному коду поиска
import random
import string
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    try:
        while True:
            if not driver.window_handles:
                break
    except:
        pass
    driver.quit()


def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}@example.com"


def test_registr_and_check_text(browser):
    # Шаг 1: логин
    browser.get("https://practicetestautomation.com/practice-test-login/")
    browser.find_element(By.NAME, "username").send_keys("student")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    # Шаг 2: проверка текста на странице
    expected_text = "Logged In Successfully"
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    page_text = browser.page_source
    assert expected_text.lower() in page_text.lower(), f"'{expected_text}' not found after login"

    # Шаг 3: ожидание 10 секунд (например, чтобы пользователь мог посмотреть на страницу)
    time.sleep(10)

    # Шаг 4: выход из аккаунта
    logout_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    )
    logout_button.click()


