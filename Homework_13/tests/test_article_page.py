import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Homework_13.Locators.article_page_locators import ArticlePageLocators
from Homework_13.utils.config_reader import read_config
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def url():
    config = read_config("config/config.ini")
    return config.get("WebDriver", "url_article")


#Перевіряє, чи відображається заголовок статті
def test_title_article(driver, open_url, accept_cookies):
    test_title = driver.find_element(By.XPATH, ArticlePageLocators.ARTICLE_TITLE)
    assert test_title.is_displayed(), "Article title is not displayed"

#Перевіряє, чи відображається дата публікації статті.
def test_post_date(driver):
    test_date = driver.find_element(By.XPATH, ArticlePageLocators.POST_DATE)
    assert test_date.is_displayed(), "Test date is not displayed"

#Перевіряє, чи відображається інформація про автора статті.
def test_author_info(driver):
    test_author = driver.find_element(By.XPATH, ArticlePageLocators.AUTHOR_INFO)
    assert test_author.is_displayed(), "Author info is not displayed"

# Клацання на кнопці коментаря, а потім перевірка відображення секції коментарів.
def test_click_comment_button(driver):
    comment_button = driver.find_element(By.XPATH, ArticlePageLocators.COMMENT_BUTTON)
    actions = ActionChains(driver)
    actions.move_to_element(comment_button).perform()
    time.sleep(1)
    comment_button.click()

    try:
        comment_section = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="shadow-host coral-shadow-host"]'))
        )
        assert comment_section.is_displayed(), "Comment section is not displayed"
    except AssertionError as e:
        raise AssertionError(e)

# Перевіряє, чи відображається віджет "Популярні" на сторінці статті.
def test_trending_widget(driver):
    trending_widget = driver.find_element(By.XPATH, ArticlePageLocators.TRENDING_WIDGET)
    assert trending_widget.is_displayed(), "Trending widget is not displayed"

#Перевіряє, чи відображається віджет "Останні" на сторінці статті.
def test_latest_widget(driver):
    latest_widget = driver.find_element(By.XPATH, ArticlePageLocators.TRENDING_WIDGET)
    assert latest_widget.is_displayed(), "Latest widget is not displayed"


