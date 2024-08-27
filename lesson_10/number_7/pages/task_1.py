from base.base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class Task1Page(BasePage):

    PAGE_URL = Links.TASK_1_PAGE  # URL 1-го задания

    # Локаторы

    ALL_INPUT_FIELDS = ("xpath", "//label")
    FIRST_NAME_LOCATOR = ("xpath", "//input[@name='first-name']")
    LAST_NAME_LOCATOR = ("xpath", "//input[@name='last-name']")
    ADDRESS_LOCATOR = ("xpath", "//input[@name='address']")
    ZIP_LOCATOR = ("xpath", "//input[@name='zip-code']")
    CITY_LOCATOR = ("xpath", "//input[@name='city']")
    COUNTRY_LOCATOR = ("xpath", "//input[@name='country']")
    EMAIL_LOCATOR = ("xpath", "//input[@name='e-mail']")
    PHONE_NUMBER_LOCATOR = ("xpath", "//input[@name='phone']")
    JOB_POSITION_LOCATOR = ("xpath", "//input[@name='job-position']")
    COMPANY_LOCATOR = ("xpath", "//input[@name='company']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")

    # Локаторы после нажатия Submit

    ZIP_CODE_LOCATOR = ("xpath", "//div[@id='zip-code']")
    ALL_FIELDS = ("xpath", "//div[contains(@class, 'alert')]")

    # Действия

    @allure.step('Вводим в поле First name - {name}')
    def enter_name(self, name: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.FIRST_NAME_LOCATOR))
            ).send_keys(name)

    @allure.step('Вводим в поле Last name - {lastname}')
    def enter_lastname(self, lastname: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.LAST_NAME_LOCATOR))
            ).send_keys(lastname)

    @allure.step('Вводим в поле Address - {address}')
    def enter_address(self, address: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.ADDRESS_LOCATOR))
            ).send_keys(address)

    @allure.step('Вводим в поле Zip code - {code}')
    def enter_zip(self, code: int) -> int:
        self.wait.until(
            EC.element_to_be_clickable((self.ZIP_LOCATOR))
            ).send_keys(code)

    @allure.step('Вводим в поле City - {city}')
    def enter_city(self, city: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.CITY_LOCATOR))
            ).send_keys(city)

    @allure.step('Вводим в поле Country - {country}')
    def enter_country(self, country: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.COUNTRY_LOCATOR))
            ).send_keys(country)

    @allure.step('Вводим в поле Email - {email}')
    def enter_email(self, email: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.EMAIL_LOCATOR))
            ).send_keys(email)

    @allure.step('Вводим в поле Phone number - {phonenumber}')
    def enter_phone(self, phonenumber: int) -> int:
        self.wait.until(
            EC.element_to_be_clickable((self.PHONE_NUMBER_LOCATOR))
            ).send_keys(phonenumber)

    @allure.step('Вводим в поле Job position - {job}')
    def enter_job(self, job: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.JOB_POSITION_LOCATOR))
            ).send_keys(job)

    @allure.step('Вводим в поле Company - {company}')
    def enter_company(self, company: str) -> str:
        self.wait.until(
            EC.element_to_be_clickable((self.COMPANY_LOCATOR))
            ).send_keys(company)

    @allure.step('Нажимаем на кнопку Submit')
    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.SUBMIT_BUTTON_LOCATOR))
            ).click()

    def check_zip_fields_color(self):
        assert "alert-danger" in self.driver.find_element(
            *self.ZIP_CODE_LOCATOR
        ).get_attribute('class'), "поле зеленое"
        print('Поле Zip code красное!')

    def check_all_fields_color(self):
        fields = self.driver.find_elements(*self.ALL_FIELDS)
        for field in fields:
            assert "success" in field.get_attribute('class'), "поле красное"
        print('Все поля зеленые!')
