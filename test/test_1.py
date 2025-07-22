import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Добавим уникальный профиль пользователя
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_registr(browser):
    browser.get("https://example.com")
    assert "Example Domain" in browser.title