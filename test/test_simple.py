import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import os

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_simple(browser):
    html = "data:text/html,<html><head><title>Hello</title></head><body>Test</body></html>"
    browser.get(html)
    assert "Hello" in browser.title

