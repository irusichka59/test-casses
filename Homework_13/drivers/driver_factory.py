from selenium import webdriver


class DriverFactory:
    @staticmethod
    def create_driver(browser):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser.lower() == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError("Invalid browser specified in config")

