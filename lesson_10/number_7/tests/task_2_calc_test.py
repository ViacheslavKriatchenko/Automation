import pytest
from base.main_test import BaseTest
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Введем данные и проверим ожидания")
@allure.tag("UI", "Automation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html",
    name="Slow calculator",
)
@allure.issue("Calc-1")
class TestCalculate(BaseTest):

    @allure.testcase("Test-1")
    @pytest.mark.ControlWork
    def test_calculator(self):

        self.task_2.open()
        self.task_2.is_opened()
        self.task_2.delay_field_clear()
        self.task_2.enter_number_in_delay_field(45)
        self.task_2.action_input()
        self.task_2.wait_delay_result()
        
        with allure.step('Проверим что текст равен ожидаемому'):
            self.task_2.result_verification()
