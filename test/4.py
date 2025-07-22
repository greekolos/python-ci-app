#универсальный код для поиска нужного слова по сайту
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest

# ===================== FIXTURE =====================
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\ASUS\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

    service = Service(ChromeDriverManager(driver_version="136.0.7103.425").install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    try:
        while True:
            if not driver.window_handles:
                break
    except:
        pass

    driver.quit()


# ===================== УНИВЕРСАЛЬНЫЙ ТЕСТ =====================
@pytest.mark.parametrize("url, expected_text", [
    ("https://www.google.com", "Поиск в Google"),
    ("https://www.wikipedia.org", "Свободная энциклопедия"),
    ("https://www.python.org", "Welcome to Python.org"),
])
def test_page_contains_text(browser, url, expected_text):
    browser.get(url)

    page_text = browser.page_source

    assert expected_text.lower() in page_text.lower(), f"'{expected_text}' not found on {url}"
