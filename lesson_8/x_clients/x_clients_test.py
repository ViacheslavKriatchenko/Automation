from x_clients_def import EmployeeDef

BASE_URL = 'https://x-clients-be.onrender.com/'

api = EmployeeDef(BASE_URL)


# проверка получения токена
def test_get_an_authorization_token():
    TOKEN = api.get_an_authorization_token()
    print(TOKEN)
    assert TOKEN is not None


""" Задание_1
проверка получить список сотрудников компании
ручные параметры: COMPANY_NAME, DESC
"""


def test_get_a_list_of_employees():
    # получить токен
    token = api.get_an_authorization_token()
    # получить список компаний
    before_all_companies_response = api.get_list_companies()
    # создать компанию
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    api.add_a_new_company(COMPANY_NAME, DESC, token)
    # получить список компаний после добавления
    after_all_companies_response = api.get_list_companies()
    # проверить что компания добавлена
    assert len(after_all_companies_response) - len(
        before_all_companies_response) == 1
    assert after_all_companies_response[-1]['name'] == COMPANY_NAME
    # записываем в переменную id созданной компании
    company_id = after_all_companies_response[-1]['id']
    data = api.get_a_list_of_employees(company_id)
    # проверяем что возвращается список сотрудников
    assert isinstance(data, list) is True


""" Задание_2
проверка создать компанию и добавить нового сотрудника
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


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


""" Задание_3
проверка создать компанию и добавить нового сотрудника
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


# проверка получить сотрудника по id
def test_get_employee_by_id():
    # получаем токен и создаем компанию
    token = api.get_an_authorization_token()
    COMPANY_NAME = 'Звездуны'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = api.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # добавить сотрудника
    FNAME = 'Люк'
    LNAME = 'Скайвокер'
    user_response = api.add_a_new_employee(FNAME, LNAME, company_id, token)
    # берем id созданного сотрудника и запрашиваем его данные
    employee_id = user_response['id']
    response = api.get_employee_by_id(employee_id)
    assert response['id'] == employee_id
    assert response['firstName'] == FNAME


""" Задание_4
проверка изменить информацию о сотруднике
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


def test_change_employee_information():
    # получаем токен и создаем компанию
    token = api.get_an_authorization_token()
    COMPANY_NAME = 'Звездуны'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = api.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # добавить сотрудника
    FNAME = 'Люк'
    LNAME = 'Скайвокер'
    user_response = api.add_a_new_employee(FNAME, LNAME, company_id, token)
    employee_id = user_response['id']
    # получить пользователя и записать значения
    body_before = api.get_employee_by_id(employee_id)
    # изменить пользователя
    NEW_LNAME = 'Вампирский'
    NEW_EMAIL = 'vamp@gmail.com'
    api.change_employee_information(employee_id, NEW_LNAME, NEW_EMAIL, token)
    # получить измененного пользователя
    body_after = api.get_employee_by_id(employee_id)
    # сверить измененные данные
    assert body_before['id'] == body_after['id']
    assert body_after['lastName'] == NEW_LNAME
    assert body_before['lastName'] != body_after['lastName']
    assert body_before['email'] != body_after['email']
