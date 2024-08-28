import pytest
from base.main_test import BaseTest
import allure


@allure.title("Тестирование заполнения формы")
@allure.description("Заполним поля формы и проверим что все данные введены")
@allure.tag("UI", "Automation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html",
    name="Data types",
)
@allure.issue("Boni-1")
class TestProfile(BaseTest):

    @allure.testcase("Test-1")
    @pytest.mark.ControlWork
    def test_input_data_and_assert_color(self):

        self.task_1.open()
        self.task_1.is_opened()
        self.task_1.enter_name("Иван")
        self.task_1.enter_lastname("Петров")
        self.task_1.enter_address("Ленина, 55-3")
        self.task_1.enter_zip("111")
        self.task_1.enter_email("test@skypro.com")
        self.task_1.enter_phone("+7985899998787")
        self.task_1.enter_city("Москва")
        self.task_1.enter_country("Россия")
        self.task_1.enter_job("QA")
        self.task_1.enter_company("SkyPro")
        self.task_1.click_submit_button()
        # self.task_1.check_zip_fields_color()

        with allure.step("Проверяем что все поля заполнены"):
            self.task_1.check_all_fields_color()
