
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 50, poll_frequency=1)

    @allure.step('Открытие сайта')
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step('Проверка что открыт сайт')
    def is_opened(self):
        self.wait.until(EC.url_to_be((self.PAGE_URL)))
