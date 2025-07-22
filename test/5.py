# регистрация и поиск нужного по универсальному коду поиска
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    ##time.sleep(10)  # задержка, чтобы браузер не закрылся сразу
    ##input("Нажми Enter чтобы закрыть браузер...")  # Ожидание ввода перед закрытием
    # Ждём, пока пользователь сам не закроет браузер
    try:
        while True:
            if not driver.window_handles:
                break
    except:
        pass

    # После закрытия браузера вручную

    driver.quit()

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{name}@example.com"

def test_registr(browser):
    browser.get("https://automationexercise.com")

    browser.find_element(By.LINK_TEXT, "Signup / Login").click()
    # Заполняем поля регистрации
    browser.find_element(By.NAME, "name").send_keys("pavel1")
    email = generate_random_email()
    browser.find_elements(By.NAME, "email")[1].send_keys(email)  # вводим в 2-е поле
    browser.find_element(By.CSS_SELECTOR, '[data-qa="signup-button"]').click()
    browser.find_element(By.ID, "id_gender1").click()
    browser.find_element(By.NAME, "password").send_keys("pavel1")
    browser.find_element(By.NAME, "days").send_keys("1")
    browser.find_element(By.NAME, "months").send_keys("May")
    browser.find_element(By.NAME, "years").send_keys("1996")
    browser.find_element(By.ID, "newsletter").click()
    browser.find_element(By.ID, "optin").click()
    browser.find_element(By.NAME, "first_name").send_keys("ggg")
    browser.find_element(By.NAME, "last_name").send_keys("www")
    browser.find_element(By.NAME, "company").send_keys("eee")
    browser.find_element(By.NAME, "address1").send_keys("rrr")
    browser.find_element(By.NAME, "address2").send_keys("ttt")
    browser.find_element(By.NAME, "country").send_keys("United States")
    browser.find_element(By.NAME, "state").send_keys("ttt")
    browser.find_element(By.NAME, "city").send_keys("yyy")
    browser.find_element(By.NAME, "zipcode").send_keys("111")
    browser.find_element(By.NAME, "mobile_number").send_keys("99999999")
    browser.find_element(By.CSS_SELECTOR, '[data-qa="create-account"]').click()

    @pytest.mark.parametrize("url, expected_text", [
        ("https://automationexercise.com/account_created", "account created!"),

    ])
    def test_page_contains_text(browser, url, expected_text):
        browser.get(url)

        page_text = browser.page_source

        assert expected_text.lower() in page_text.lower(), f"'{expected_text}' not found on {url}"

