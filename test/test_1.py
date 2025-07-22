## регистрация на сайте
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
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


def test_registr(browser):
    browser.get("http://users.bugred.ru/user/login/index.html")
    # Нажимаем на "Регистрация"



    # Заполняем поля регистрации
    browser.find_element(By.NAME, "name").send_keys("Pavel")
    browser.find_element(By.NAME, "email").send_keys("pavel1@yandex.ru")
    password_fields = browser.find_elements(By.NAME, "password")
    password_fields[1].send_keys("pavel")  # вводим в 2-е поле

    # Нажимаем на кнопку "Зарегистрироваться"
    browser.find_element(By.XPATH, '//input[@value="Зарегистрироваться"]').click()

    # Подождем немного, чтобы увидеть результат
    time.sleep(2)