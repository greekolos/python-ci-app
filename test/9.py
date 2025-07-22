## запрещенные слова на сайте

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Список запрещённых слов
FORBIDDEN_WORDS = ["порно", "сепкс", "минпет"]

# Фикстура для запуска и завершения браузера
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


def test_check_forbidden_words(browser):
    # Открываем указанный сайт
    browser.get("https://video.porno365s.me/")

    # Получаем весь текст на странице (внутри <body>)
    page_text = browser.find_element(By.TAG_NAME, "body").text.lower()

    # Проходим по каждому запрещённому слову и проверяем его наличие
    for word in FORBIDDEN_WORDS:
        if word.lower() in page_text:
            print(f"❌ Найдено запрещённое слово: {word}")
            pytest.fail(f"Обнаружено запрещённое слово: {word}")  # Прерываем тест с ошибкой
        else:
            #Если цикл завершился без обнаружения слов
            print("✅ Запрещённых слов не найдено.")
