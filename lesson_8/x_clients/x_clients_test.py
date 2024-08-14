from x_clients_def import EmployeeDef

BASE_URL = 'https://x-clients-be.onrender.com/'

api = EmployeeDef(BASE_URL)


# проверка получения токена
def test_get_an_authorization_token():
    TOKEN = api.get_an_authorization_token()
    print(TOKEN)
    assert TOKEN is not None


# проверка списка компаний
def test_get_list_companies():
    response = api.get_list_companies()
    assert len(response) > 0
    assert response[2]['name'] == 'Муж на час'


# проверка получить список сотрудников компании
def test_get_a_list_of_employees():
    company_id = 242
    data = api.get_a_list_of_employees(company_id)
    assert isinstance(data, list) is True


# проверка добавить нового сотрудника
def test_add_a_new_employee():
    company_id = 740
    # список до добавления сотрудника
    body_before = api.get_a_list_of_employees(company_id)
    list_before = len(body_before)
    # добавить сотрудника
    TOKEN = api.get_an_authorization_token()
    fname = 'Сатан'
    lname = 'Сатанский'
    api.add_a_new_employee(fname, lname, company_id, TOKEN)
    # список после добавления сотрудника
    body_after = api.get_a_list_of_employees(company_id)
    list_after = len(body_after)
    # сравнение списка
    assert list_after - list_before == 1
    assert body_after[-1]['firstName'] == fname


# проверка получить сотрудника по id
def test_get_employee_by_id():
    employee_id = 819
    response = api.get_employee_by_id(employee_id)
    assert response['id'] == employee_id


# проверка изменить информацию о сотруднике
def test_change_employee_information():
    employee_id = 837
    # получить пользователя и записать значения
    body_before = api.get_employee_by_id(employee_id)
    # получить токен
    TOKEN = api.get_an_authorization_token()
    # изменить пользователя
    new_lname = 'Вампирский'
    new_email = 'vamp@gmail.com'
    api.change_employee_information(employee_id, new_lname, new_email, TOKEN)
    # получить измененного пользователя
    body_after = api.get_employee_by_id(employee_id)
    # сверить измененные данные
    assert body_before['id'] == body_after['id']
    assert body_after['lastName'] == new_lname
    assert body_before['lastName'] != body_after['lastName']
