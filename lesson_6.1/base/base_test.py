import pytest
from pages.task_1 import Task1Page
from pages.task_2 import Task2Page
from pages.task_3 import Task3Page


class BaseTest:

    task_1: Task1Page
    task_2: Task2Page
    task_3: Task3Page

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.task_1 = Task1Page(driver)
        request.cls.task_2 = Task2Page(driver)
        request.cls.task_3 = Task3Page(driver)
