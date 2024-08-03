import pytest
from base.base_test import BaseTest


class TestCalculate(BaseTest):

    @pytest.mark.ControlWork
    def test_calculator(self):

        self.task_2.open()
        self.task_2.is_opened()
        self.task_2.delay_field_clear()
        self.task_2.enter_number_in_delay_field(45)
        self.task_2.action_input()
        self.task_2.wait_delay_result()
        self.task_2.result_verification()
