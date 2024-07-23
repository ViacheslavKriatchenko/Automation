from base.base_page import BasePage
from links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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

    def enter_login(self):
        self.wait.until(
            EC.element_to_be_clickable((self.USERNAME_FIELD_LOCATOR))
            ).send_keys('standard_user')

    def enter_password(self):
        self.wait.until(
            EC.element_to_be_clickable((self.PASSWORD_FIELD_LOCATOR))
            ).send_keys('secret_sauce')

    def click_login_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.LOGIN_BUTTON_LOCATOR))
            ).click()

    def add_to_cart_Sauce_Labs_Backpack(self):
        self.wait.until(
            EC.element_to_be_clickable((self.Sauce_Labs_Backpack_CART_LOCATOR))
        ).click()

    def add_to_cart_Sauce_Labs_Bolt_T_Shirt(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (self.Sauce_Labs_Bolt_T_Shirt_CART_LOCATOR)
                )
        ).click()

    def add_to_cart_Sauce_Labs_Onesie(self):
        self.wait.until(
            EC.element_to_be_clickable((self.Sauce_Labs_Onesie_CART_LOCATOR))
        ).click()

    def go_to_the_cart(self):
        self.driver.get('https://www.saucedemo.com/cart.html')

    def click_checkout_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.CHECKOUT_BUTTON_LOCATOR))
        ).click()

    def enter_firstname(self, name):
        self.wait.until(
            EC.element_to_be_clickable((self.FIRSTNAME_FIELD_LOCATOR))
        ).send_keys(name)

    def enter_lastname(self, lastname):
        self.wait.until(
            EC.element_to_be_clickable((self.LASTNAME_FIELD_LOCATOR))
        ).send_keys(lastname)

    def enter_postalcode(self, code):
        self.wait.until(
            EC.element_to_be_clickable((self.POSTALCODE_FIELD_LOCATOR))
        ).send_keys(code)

    def click_continue_button(self):
        self.wait.until(
            EC.element_to_be_clickable((self.CONTINUE_BUTTON_LOCATOR))
        ).click()

    def print_total_price(self):
        total = self.driver.find_element(*self.TOTAL_PRICE_FIELD)
        print(f'Total price = {total}')

    def result_verification(self):
        assert self.driver.find_element(
            *self.SCREEN_LOCATOR
            ).text == '15', "Что-то пошло не так"
