puthon -m venv venv  
python -m pip freeze > requirements.txt  
python -m pip install -r requirements.txt  

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
def add_a_new_company(self, company_name, desc, TOKEN):
        response = requests.post(
            url=f'{self.url}company',
            headers={
                'x-client-token': TOKEN
            },
            json={
                'name': company_name,
                'description': desc
            }
        )
        return response.json()

from x_clients_def import EmployeeDef
BASE_URL = 'https://x-clients-be.onrender.com/'
api = EmployeeDef(BASE_URL)

def test_add_a_new_employee():
    # получаем токен и создаем компанию
    token = api.get_an_authorization_token()
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = api.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # список до добавления сотрудника
    body_before = api.get_a_list_of_employees(company_id)
    list_before = len(body_before)
    # добавить сотрудника
    FNAME = 'Зомби'
    LNAME = 'Разлагайченко'
    api.add_a_new_employee(FNAME, LNAME, company_id, token)
    # список после добавления сотрудника
    body_after = api.get_a_list_of_employees(company_id)
    list_after = len(body_after)
    # сравнение списка и имени созданного сотрудника
    assert list_after - list_before == 1
    assert body_after[-1]['firstName'] == FNAME
```
### 9 Урок
+ SQLAlchemy. Подключение и select-запросы
+ SQLAlchemy. Запросы insert, update и delete  
  ***Пример***
```
from sqlalchemy import create_engine, text

db_connection_path = ("postgresql://sait_name:"
                      "gagg87dg687D5G785g875G8G@"
                      "dhd-adga6h7Hh8a8ha-a.piupupu-postgres.render.com/"
                      "sait_name_fxd0")
class DbTable():

def __init__(self, db_connection_path) -> None:
        self.db = create_engine(db_connection_path)

def get_employee_info_by_id(self, emp_id):
        sql = text('select * from employee where id= :id')
        return self.db.execute(sql, id=emp_id).fetchall()
```
### 10 Урок
+ Allure - Разметка тестов, шагов, методов
+ Автоматизация отчета  
  ***Пример***
```
```
