from base.base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure


class Task3Page(BasePage):

    PAGE_URL = Links.TASK_3_PAGE  # URL 3-го задания

    # Локаторы

    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//input[@id='login-button']")
    Sauce_Labs_Backpack_CART_LOCATOR = (
        "xpath", "//button[@id='add-to-cart-sauce-labs-backpack']"
        )
    Sauce_Labs_Bolt_T_Shirt_CART_LOCATOR = (
        "xpath", "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    )
    Sauce_Labs_Onesie_CART_LOCATOR = (
        "xpath", "//button[@id='add-to-cart-sauce-labs-onesie']"
    )
    CHECKOUT_BUTTON_LOCATOR = (
        "xpath", "//button[@id='checkout']"
    )
    FIRSTNAME_FIELD_LOCATOR = (
        "xpath", "//input[@id='first-name']"
    )
    LASTNAME_FIELD_LOCATOR = (
        "xpath", "//input[@id='last-name']"
    )
    POSTALCODE_FIELD_LOCATOR = (
        "xpath", "//input[@id='postal-code']"
    )
    CONTINUE_BUTTON_LOCATOR = (
        "xpath", "//input[@id='continue']"
    )
    TOTAL_PRICE_FIELD = (
        "xpath", "//div[@class='summary_total_label']"
    )

    # Действия

    @allure.step('Вводим в поле Login - standard_user')
    def enter_login(self):
        self.wait.until(
            EC.element_to_be_clickable((self.USERNAME_FIELD_LOCATOR))
            ).send_keys('standard_user')

    @allure.step('Вводим в поле Password - secret_sauce')
    def enter_password(self):
        self.wait.until(
            EC.element_to_be_clickable((self.PASSWORD_FIELD_LOCATOR))
            ).send_keys('secret_sauce')

    @allure.step('Жмякаем кнопку Войти')
    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.LOGIN_BUTTON_LOCATOR))
            ).click()

    @allure.step('Нажимаем на кнопку корзина на товаре Sauce_Labs_Backpack')
    def add_to_cart_Sauce_Labs_Backpack(self):
        self.wait.until(
            EC.element_to_be_clickable((self.Sauce_Labs_Backpack_CART_LOCATOR))
        ).click()

    @allure.step('Нажимаем на кнопку корзина на товаре Sauce_Labs_Bolt_T_Shirt')
    def add_to_cart_Sauce_Labs_Bolt_T_Shirt(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (self.Sauce_Labs_Bolt_T_Shirt_CART_LOCATOR)
                )
        ).click()

    @allure.step('Нажимаем на кнопку корзина на товаре Sauce_Labs_Onesie')
    def add_to_cart_Sauce_Labs_Onesie(self):
        self.wait.until(
            EC.element_to_be_clickable((self.Sauce_Labs_Onesie_CART_LOCATOR))
        ).click()

    @allure.step('Переходим в корзину')
    def go_to_the_cart(self):
        self.driver.get('https://www.saucedemo.com/cart.html')

    @allure.step('Нажимаем кнопку CHECKOUT')
    def click_checkout_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.CHECKOUT_BUTTON_LOCATOR))
        ).click()

    @allure.step('Вводим в поле First name - {name}')
    def enter_firstname(self, name):
        self.wait.until(
            EC.element_to_be_clickable((self.FIRSTNAME_FIELD_LOCATOR))
        ).send_keys(name)

    @allure.step('Вводим в поле Last name - {lastname}')
    def enter_lastname(self, lastname):
        self.wait.until(
            EC.element_to_be_clickable((self.LASTNAME_FIELD_LOCATOR))
        ).send_keys(lastname)

    @allure.step('Вводим в поле Zip/Postal code - {code}')
    def enter_postalcode(self, code):
        self.wait.until(
            EC.element_to_be_clickable((self.POSTALCODE_FIELD_LOCATOR))
        ).send_keys(code)

    @allure.step('Нажимаем кнопку CONTINUE')
    def click_continue_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.CONTINUE_BUTTON_LOCATOR))
        ).click()

    def print_total_price(self):
        total_text = self.driver.find_element(*self.TOTAL_PRICE_FIELD).text
        print(total_text)

    def result_verification(self):
        assert '$58.29' in self.driver.find_element(
            *self.TOTAL_PRICE_FIELD
            ).text, 'Неверная цена'
        print('Всё ОК!')
