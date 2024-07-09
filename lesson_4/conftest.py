"""
файл для общей структуры,
хранит в себе фикстуры, инициализации, настройки.
Можно разделить по типу на юнит, интерграцию
и в каждом разделе сделать свой конф

Например выбор браузера:

def pytest_addoption(parser):
    parser.addoption(
    "--.browser,
    default = "chrome",
    choices = ("chrome", "firefox")
    )

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
"""
