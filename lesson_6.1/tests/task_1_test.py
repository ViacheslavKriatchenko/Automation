import pytest
from base.base_test import BaseTest


class TestProfile(BaseTest):

    @pytest.mark.ControlWork
    def test_input_data_and_assert_color(self):

        self.task_1.open()
        self.task_1.is_opened()
        self.task_1.enter_name('Иван')
        self.task_1.enter_lastname('Петров')
        self.task_1.enter_address('Ленина, 55-3')
        self.task_1.enter_email('test@skypro.com')
        self.task_1.enter_phone('+7985899998787')
        self.task_1.enter_city('Москва')
        self.task_1.enter_country('Россия')
        self.task_1.enter_job('QA')
        self.task_1.enter_company('SkyPro')
        self.task_1.click_submit_button()
        self.task_1.check_zip_fields_color()
        self.task_1.check_all_fields_color()
