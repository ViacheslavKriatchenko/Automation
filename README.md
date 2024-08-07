# lessons_Python_Automation
### 1 Урок:
Типы данных. Понятие переменной  
+ Списки  
+ Функции  
+ Области видимости переменной  
+ Стек вызовов  
  ***Пример:***
```
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
print(f'Вас зовут: {first_name} {last_name}')
```
### 2 Урок:
+ Ветвления. Условные операторы  
+ Циклы  
+ Логические операторы  
  ***Пример:***
```
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2 = []
for i in range(0, len(lst)):
    if lst[i] < 30 and lst[i] % 3 == 0:
        lst2.append(lst[i])
print(lst2)
```
### 3 Урок:
+ Основные понятия ООП  
+ Методы и поля класса  
+ Взаимодействие классов  
+ Вложенные классы  
  ***Пример***
```
class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('user created')

    def greeting(self):
        print(f'{self.name} says HELLO!')


class Student(Person):

    def __init__(self, name, age, average_grade) -> None:
        super().__init__(name, age)
        self.average_grade = average_grade

    def greeting(self):
        print(f'Student with name {self.name} says HELLO!')
```
### 4 Урок
+ Разработка калькулятора
+ Тестирование калькулятора
+ Более сложные автотесты
+ Маркеры и параметризация тестов  
  ***Пример***
```
@pytest.mark.negative
@pytest.mark.parametrize('input, output, expectation', [
    ('!you', '!you', does_not_raise()),
    ('12level', '12level', does_not_raise()),
    (None, None, pytest.raises(AttributeError)),
    ])
def test_check_capitilize_negative(input, output, expectation):
    with expectation:
        result = StringUtils().capitilize(input)
        assert output == result
```
### 5 Урок
+ Знакомство с Selenium
+ Базовые методы Selenium
+ Локаторы
+ Автоматизация сбора данных  
  ***Пример***
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://the-internet.herokuapp.com/entry_ad'

driver.get(url)

button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(('xpath', "//p[text()='Close']"))
    )
button.click()
```
### 6 Урок
+ Методы get_title и current_url
+ Работа с cookie
+ Изменение размеров окна браузера
+ Работа с элементами на странице
+ Работа с атрибутами элементов
+ Методы is_enabled, is_displayed и is_selected
+ Работа с вложенными элементами и группами элементов
+ Методы quit и close
+ Ожидания  
  ***Пример***
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Создание экземпляра вэбдрайвера
options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1)

# Переход на вэб-страницу
URL = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
driver.get(URL)

# Ожидание загрузки элементов пока крутится спиннер
SPINNER = ("xpath", "//span[@id='spinner']")
wait.until(EC.invisibility_of_element_located((SPINNER)))

# Вытаскивам информацию из атрибута
THIRD_PICTURE = ("xpath", "(//div[@id='image-container']//img)[3]")
THIRD_PICTURE_DATA = driver.find_element(*THIRD_PICTURE).get_attribute("src")

# Вывод на печать информации
print(f'Содержимое атрибута src - {THIRD_PICTURE_DATA}')
```
### 7 Урок
+ Что такое Page Object  
  ***Пример***
```
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
```
### 8 Урок
+ Знакомство с библиотекой Requests
+ Теория, практика, сложные структуры  
  ***Пример***
```
```
