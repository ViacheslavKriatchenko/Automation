from base.base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Task2Page(BasePage):

    PAGE_URL = Links.TASK_2_PAGE  # URL 2-го задания

    # Локаторы

    DELAY_FIELD_LOCATOR = ("xpath", "//input[@id='delay']")
    NUMBER_7_LOCATOR = ("xpath", "//span[text()='7']")
    NUMBER_8_LOCATOR = ("xpath", "//span[text()='8']")
    PLUS_LOCATOR = ("xpath", "//span[text()='+']")
    EQUIL_LOCATOR = ("xpath", "//span[text()='=']")
    SCREEN_LOCATOR = ("xpath", "//div[@class='screen']")

    # Действия

    def delay_field_clear(self):
        self.wait.until(
            EC.element_to_be_clickable((self.DELAY_FIELD_LOCATOR))
            ).clear()

    def enter_number_in_delay_field(self, number):
        self.wait.until(
            EC.element_to_be_clickable((self.DELAY_FIELD_LOCATOR))
            ).send_keys(number)

    def action_input(self):
        action = ActionChains(self.driver)
        action.click(self.driver.find_element(*self.NUMBER_7_LOCATOR))
        action.pause(2)
        action.click(self.driver.find_element(*self.PLUS_LOCATOR))
        action.pause(2)
        action.click(self.driver.find_element(*self.NUMBER_8_LOCATOR))
        action.pause(2)
        action.click(self.driver.find_element(*self.EQUIL_LOCATOR))
        action.perform()

    def wait_delay_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element((self.SCREEN_LOCATOR), '15')
        )

    def result_verification(self):
        assert self.driver.find_element(
            *self.SCREEN_LOCATOR
            ).text == '15', "Что-то пошло не так"
