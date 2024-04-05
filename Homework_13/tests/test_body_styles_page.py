import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Homework_13.Locators.body_styles_page_locators import BodyStylesPageLocators
from Homework_13.utils.config_reader import read_config


@pytest.fixture(scope="module")
def url():
    config = read_config("config/config.ini")
    return config.get("WebDriver", "url_body_styles")


def test_find_block_head(driver, open_url, accept_cookies):

    # Знайти елемент блоку заголовку
    block_head = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, BodyStylesPageLocators.BLOCK_HEAD))
    )
    assert block_head.is_displayed(), "Block head is not visible"


def test_find_find_vehicle_wrapper(driver):

    # Знайти елемент обгортки пошуку транспортних засобів
    find_vehicle_wrapper = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, BodyStylesPageLocators.FIND_VEHICLE_WRAPPER))
    )
    assert find_vehicle_wrapper.is_displayed(), "Find vehicle wrapper is not displayed"


def test_find_first_vehicle_link(driver):

    # Знайти перше посилання на транспортний засіб
    first_vehicle_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, BodyStylesPageLocators.FIRST_VEHICLE_LINK))
    )
    assert first_vehicle_link.is_displayed(), "First vehicle link is not visible"
