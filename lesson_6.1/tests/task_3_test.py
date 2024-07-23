import pytest
from base.base_test import BaseTest
from time import sleep


class TestTotalPrice(BaseTest):

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
        sleep(5)
