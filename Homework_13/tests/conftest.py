import pytest
from selenium import webdriver
from Homework_13.drivers.driver_factory import DriverFactory
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Homework_13.Locators.layout_page_locators import LayoutLocators


@pytest.fixture(scope="module")
def driver():
    # Ініціалізуємо драйвер, наприклад, Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()  # Максимізуємо вікно браузера
    yield driver
    # Закриваємо драйвер після завершення тестів
    driver.quit()


@pytest.fixture(scope="module")
def open_url(driver, url):
    driver.get(url)


@pytest.fixture(scope="function")
def accept_cookies(driver):
    # Перейти на сторінку
    # driver.get(url)

    # Перевірити наявність кнопки прийняття файлів cookie
    try:
        accept_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, LayoutLocators.COOKIES_BUTTON))
        )
    except:
        accept_btn = None

    # Прийняти файли cookie, якщо кнопка доступна
    if accept_btn:
        accept_btn.click()
        # Додаткова затримка для оновлення сторінки після кліку
        time.sleep(3)

    yield


@pytest.fixture(scope="session")
def browser():
    browser = DriverFactory.create_driver("chrome")
    yield browser
    browser.quit()

