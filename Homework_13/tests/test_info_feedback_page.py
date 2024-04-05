
import pytest
import random
import string

from selenium.webdriver.common.by import By
from Homework_13.Locators.info_feedback_locators import InfoFeedbackLocators
from Homework_13.utils.config_reader import read_config


@pytest.fixture(scope="module")
def url():
    config = read_config("config/config.ini")
    return config.get("WebDriver", "url_info_feedback")


def generate_random_name():
    # Генеруємо випадкове ім'я, використовуючи великі та малі літери
    name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    return name


def generate_random_email():
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for i in range(10)) + "@example.com"
    return email


def test_info_feedback_block(driver, open_url, accept_cookies):
    feedback_block = driver.find_element(By.XPATH, InfoFeedbackLocators.INFO_FEEDBACK_BLOCK)
    assert feedback_block.is_displayed(), "Feedback_block is not displayed"


def test_name_feedback_block(driver):
    name_feedback_block = driver.find_element(By.XPATH, InfoFeedbackLocators.NAME_INPUT)
    assert name_feedback_block.is_displayed(), "Name feedback block is not displayed"

    name = generate_random_name() # Генеруємо випадкове ім'я
    name_feedback_block.send_keys(name) # Введення випадкового імені в поле
    # Перевірка, чи введене ім'я відображається в полі вводу
    assert name_feedback_block.get_attribute("value") == name, "Name input value is not set correctly"


def test_email_feedback_block(driver):
    email_feedback_block = driver.find_element(By.XPATH, InfoFeedbackLocators.EMAIL_INPUT)
    assert email_feedback_block.is_displayed(), "Name feedback block is not displayed"

    email = generate_random_email()
    email_feedback_block.send_keys(email)
    assert email_feedback_block.get_attribute("value") == email, "Email input value is not set correctly"


def test_message_feedback_block(driver):
    message_feedback_block = driver.find_element(By.XPATH, InfoFeedbackLocators.MESSAGE)
    assert message_feedback_block.is_displayed(), "Message feedback block is not displayed"
    message_text = "Test message"
    message_feedback_block.send_keys(message_text)
    assert message_feedback_block.get_attribute("value") == message_text, "Message input value is not set correctly"


# Розкоментувати тест тільки для перевірки відправки відгуку! не частіше 1 раз на день
# def test_click_submit_button(driver):
#     submit_button = driver.find_element(By.XPATH, InfoFeedbackLocators.SUBMIT_BUTTON)
#     actions = ActionChains(driver)
#     actions.move_to_element(submit_button).perform()
#     submit_button.click()
#
#     try:
#         submit_section = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, '//div[@class="message item visible"]'))
#         )
#     except TimeoutException:
#         # Обробка помилки, якщо елемент не було знайдено протягом вказаного часу очікування
#         print("Element not found within the specified time.")

