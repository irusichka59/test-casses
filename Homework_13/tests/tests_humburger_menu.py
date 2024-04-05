import time

import pytest
from selenium.webdriver.common.by import By
from Homework_13.Locators.layout_page_locators import LayoutLocators
from Homework_13.utils.config_reader import read_config


@pytest.fixture(scope="module")
def url():
    config = read_config("config/config.ini")
    return config.get("WebDriver", "url")


def test_hamburger_menu_button(driver, open_url, accept_cookies):
    hamburger_menu_button = driver.find_element(By.XPATH, LayoutLocators.HUMBURGER_BUTTON)
    assert hamburger_menu_button.is_displayed(), "Hamburger menu is not displayed"

    # Клік на знайдений елемент
    hamburger_menu_button.click()
    time.sleep(5)  # час на очікування після відкриття меню,це обовʼязково щоб встигли відпрацювати наступні тести
    # Очікуваний результат - кнопка логін
    expected_login_button = driver.find_element(By.XPATH, LayoutLocators.LOGIN_BUTTON)
    assert expected_login_button.is_displayed(), "Login button is not displayed"


def test_dropdown_toggle(driver):
    # Знаходження всіх дропдаунів
    dropdown_toggles = driver.find_elements(By.XPATH, LayoutLocators.DROPDOWN_TOGGLE)
    assert len(dropdown_toggles) > 0, "No dropdown toggles found"

    # Клік на перший дропдаун
    first_dropdown_toggle = dropdown_toggles[0]
    assert first_dropdown_toggle.is_displayed(), "First dropdown toggle is not displayed"
    first_dropdown_toggle.click()
    time.sleep(2) #для себе зробила, щоб можна бууло побачити відкриття дропдаун, це не обовʼязково

    # Очікування першого дропдауну
    first_dropdown = driver.find_element(By.XPATH, "//li[@class='dropdown-wrapper']")
    assert first_dropdown.is_displayed(), "First dropdown is not displayed"


def test_menu_box(driver):
    # Знаходження елементу menu_box
    menu_box = driver.find_element(By.XPATH, LayoutLocators.MENU_BOX)
    # Прокрутка до елементу menu_box
    driver.execute_script("arguments[0].scrollIntoView();", menu_box)
    # Перевірка відображення блоку меню
    assert menu_box.is_displayed(), "Menu box is not displayed"
    # Перевірка відображення логотипу гамбургер меню
    expected_logo = driver.find_element(By.XPATH, LayoutLocators.HUMBURGER_MENU_LOGO)
    assert expected_logo.is_displayed(), "Hamburger menu logo is not displayed"


def test_hamburger_menu_animated_block(driver):
    animated_block = driver.find_element(By.XPATH, LayoutLocators.HUMBURGER_MENU_ANIMATED_BLOCK)
    assert animated_block.is_displayed(), "Hamburger menu animated block is not displayed"


def test_msn_menu(driver):
    msn_menu = driver.find_element(By.XPATH, LayoutLocators.MSN_MENU)
    assert msn_menu.is_displayed(), "MSN menu is not displayed"
    # Перевірка кількості елементів в MSN_MENU
    menu_items = msn_menu.find_elements(By.XPATH, ".//li")
    assert len(menu_items) == 5, "The MSN menu does not have 5 items"
