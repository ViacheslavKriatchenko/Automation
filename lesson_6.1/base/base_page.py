
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 50, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be((self.PAGE_URL)))
