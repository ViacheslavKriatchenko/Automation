from base.base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC


class Task1Page(BasePage):

    PAGE_URL = Links.TASK_1_PAGE  # URL 1-го задания

    # Локаторы

    ALL_INPUT_FIELDS = ("xpath", "//label")
    FIRST_NAME_LOCATOR = ("xpath", "//input[@name='first-name']")
    LAST_NAME_LOCATOR = ("xpath", "//input[@name='last-name']")
    ADDRESS_LOCATOR = ("xpath", "//input[@name='address']")
    ZIP_CODE_LOCATOR = ("xpath", "//input[@name='zip-code']")
    CITY_LOCATOR = ("xpath", "//input[@name='city']")
    COUNTRY_LOCATOR = ("xpath", "//input[@name='country']")
    EMAIL_LOCATOR = ("xpath", "//input[@name='e-mail']")
    PHONE_NUMBER_LOCATOR = ("xpath", "//input[@name='phone']")
    JOB_POSITION_LOCATOR = ("xpath", "//input[@name='job-position']")
    COMPANY_LOCATOR = ("xpath", "//input[@name='company']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")

    # Действия

    def enter_name(self, name):
        self.wait.until(
            EC.element_to_be_clickable((self.FIRST_NAME_LOCATOR))
            ).send_keys(name)

    def enter_lastname(self, lastname):
        self.wait.until(
            EC.element_to_be_clickable((self.LAST_NAME_LOCATOR))
            ).send_keys(lastname)

    def enter_address(self, address):
        self.wait.until(
            EC.element_to_be_clickable((self.ADDRESS_LOCATOR))
            ).send_keys(address)

    def enter_city(self, city):
        self.wait.until(
            EC.element_to_be_clickable((self.CITY_LOCATOR))
            ).send_keys(city)

    def enter_country(self, country):
        self.wait.until(
            EC.element_to_be_clickable((self.COUNTRY_LOCATOR))
            ).send_keys(country)

    def enter_email(self, email):
        self.wait.until(
            EC.element_to_be_clickable((self.EMAIL_LOCATOR))
            ).send_keys(email)

    def enter_phone(self, phonenumber):
        self.wait.until(
            EC.element_to_be_clickable((self.PHONE_NUMBER_LOCATOR))
            ).send_keys(phonenumber)

    def enter_job(self, job):
        self.wait.until(
            EC.element_to_be_clickable((self.JOB_POSITION_LOCATOR))
            ).send_keys(job)

    def enter_company(self, company):
        self.wait.until(
            EC.element_to_be_clickable((self.COMPANY_LOCATOR))
            ).send_keys(company)

    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SUBMIT_BUTTON_LOCATOR))
            ).click()

    def check_fields_color(self):
        self.all_fields = self.driver.f(*self.ALL_INPUT_FIELDS)
        for self.field in self.all_fields:
            assert "alert-success" in self.all_fields.get_attribute('class'), "поле красное"
