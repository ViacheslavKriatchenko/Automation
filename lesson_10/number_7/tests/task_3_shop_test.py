import pytest
from base.main_test import BaseTest
import allure


@allure.title("Тестирование корзины")
@allure.description("Оформим корзину и сверим итоговую сумму")
@allure.tag("UI", "Automation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://www.saucedemo.com",
    name="Swag Labs",
)
@allure.issue("Cart-1")
class TestTotalPrice(BaseTest):

    @allure.testcase("Test-1")
    @pytest.mark.ControlWork
    def test_total_price(self):

        self.task_3.open()
        self.task_3.is_opened()
        self.task_3.enter_login()
        self.task_3.enter_password()
        self.task_3.click_login_button()
        self.task_3.add_to_cart_Sauce_Labs_Backpack()
        self.task_3.add_to_cart_Sauce_Labs_Bolt_T_Shirt()
        self.task_3.add_to_cart_Sauce_Labs_Onesie()
        self.task_3.go_to_the_cart()
        self.task_3.click_checkout_button()
        self.task_3.enter_firstname('Slava')
        self.task_3.enter_lastname('I\'m doing magic')
        self.task_3.enter_postalcode(12345)
        self.task_3.click_continue_button()
        self.task_3.print_total_price()

        with allure.step('Сверим итоговую сумму корзины'):
            self.task_3.result_verification()
