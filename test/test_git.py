import random
import string
import pytest
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless=new")  # запуск без GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    # Создаём уникальную временную директорию для профиля
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    driver.quit()
    shutil.rmtree(user_data_dir, ignore_errors=True)


def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}@example.com"


def test_registr_and_check_text(browser):
    browser.get("https://practicetestautomation.com/practice-test-login/")

    # Вводим логин и пароль
    browser.find_element(By.NAME, "username").send_keys("student")
    browser.find_element(By.ID, "password").send_keys("Password123")
    browser.find_element(By.ID, "submit").click()

    # Ждём появление текста "Logged In Successfully" на странице
    expected_text = "Logged In Successfully"
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected_text)
    )

    page_text = browser.page_source
    assert expected_text.lower() in page_text.lower(), f"'{expected_text}' not found after login"

    # Ждём и кликаем по кнопке выхода
    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
    )
    logout_button.click()

    # Можно дополнительно проверить, что после выхода мы вернулись на страницу логина
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "submit"))
    )

