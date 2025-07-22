## работаем в яндекс браузере, открываем сайт и сраниваем есть ли нужное слова
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\ASUS\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

    # Указываем точную версию chromedriver под версию браузера
    service = Service(ChromeDriverManager(driver_version="136.0.7103.425").install())

    driver = webdriver.Chrome(service=service, options=options)
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
def test_registr(browser):
    browser.get("https://www.google.com")

    # Ждём появления кнопки
    btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "btnK")))

    # Получаем текст из атрибута value
    message_text = btn.get_attribute("value")

    assert message_text == "Поиск в Google", f"Actual message: [{message_text}]"


