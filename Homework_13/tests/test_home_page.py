import pytest
from selenium.webdriver.common.by import By
from Homework_13.Locators.home_page_locators import HomepageLocators
from Homework_13.Locators.layout_page_locators import LayoutLocators
from Homework_13.utils.config_reader import read_config


@pytest.fixture(scope="module")
def url():
    config = read_config("config/config.ini")
    return config.get("WebDriver", "url")


def test_search_input_field(driver, open_url, accept_cookies):
    search_input = driver.find_element(By.XPATH, LayoutLocators.SEARCH_INPUT)
    assert search_input.is_displayed(), "Search input is not displayed"


def test_search_button(driver):
    search_button = driver.find_element(By.XPATH, LayoutLocators.SEARCH_BUTTON)
    assert search_button.is_displayed(), "Search button is not displayed"


def test_title_logo(driver):
    logo_title = driver.find_element(By.XPATH, LayoutLocators.LOGO_TITLE)
    assert logo_title.is_displayed(), "Title logo is not displayed"


def test_hamburger_menu_button(driver):
    hamburger_menu_button = driver.find_element(By.XPATH, LayoutLocators.HUMBURGER_BUTTON)
    assert hamburger_menu_button.is_displayed(), "Hamburger menu is not displayed"


def test_top_slider_button(driver):
    top_slider_button = driver.find_element(By.XPATH, HomepageLocators.TOP_SLIDER_BUTTON)
    assert top_slider_button.is_displayed(), "Top slider is not displayed"


def test_filmstrip_widget_reviews(driver):
    filmstrip = driver.find_element(By.XPATH, HomepageLocators.FILMSTRIP_WIDGET_REVIEWS)
    assert filmstrip.is_displayed(), "Filmstrip is not displayed"
