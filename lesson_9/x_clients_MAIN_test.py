from x_clients_company_def import CompanyDef
from x_clients_employee_def import EmployeeDef
from x_clients_db_def import DbTable

BASE_URL = 'https://x-clients-be.onrender.com/'
db_connection_path = ("postgresql://x_clients_user:"
                      "95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@"
                      "dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/"
                      "x_clients_db_fxd0")

apiC = CompanyDef(BASE_URL)
apiE = EmployeeDef(BASE_URL)
db = DbTable(db_connection_path)


# проверка получения токена
def test_get_an_authorization_token():
    TOKEN = apiC.get_an_authorization_token()
    print(TOKEN)
    assert TOKEN is not None


""" Задание_1
проверка получить список сотрудников компании
ручные параметры: COMPANY_NAME, DESC
"""


def test_get_a_list_of_employees():
    # получить токен
    token = apiC.get_an_authorization_token()
    # получить список компаний
    before_all_companies_response = apiC.get_list_companies()
    before_all_companies_response_db = db.get_all_companies()
    # создать компанию
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    apiC.add_a_new_company(COMPANY_NAME, DESC, token)
    # получить список компаний после добавления
    after_all_companies_response = apiC.get_list_companies()
    # записываем в переменную id созданной компании
    company_id = after_all_companies_response[-1]['id']
    data = apiE.get_a_list_of_employees(company_id)
    # *** удаление созданной компании в БД
    db.delete_company(company_id)
    # *** сравниваем длину списка базы и свагера
    assert len(before_all_companies_response) == len(before_all_companies_response_db)
    # проверить что компания добавлена
    assert len(after_all_companies_response) - len(
        before_all_companies_response) == 1
    assert after_all_companies_response[-1]['name'] == COMPANY_NAME
    # проверяем что возвращается список сотрудников
    assert isinstance(data, list) is True


""" Задание_2
проверка создать компанию и добавить нового сотрудника
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


def test_add_a_new_employee():
    # получаем токен и создаем компанию
    token = apiC.get_an_authorization_token()
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = apiC.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # *** проверяем что в базе создалась компания и id равны
    assert company_id == db.get_max_company_id()[0][0]
    # список до добавления сотрудника
    body_before = apiE.get_a_list_of_employees(company_id)
    list_before = len(body_before)
    # добавить сотрудника
    FNAME = 'Зомби'
    LNAME = 'Разлагайченко'
    apiE.add_a_new_employee(FNAME, LNAME, company_id, token)
    db_employee_id = db.get_employee_info_max_id()[0][0]
    # *** сравниваем введенное имя с именем в БД посл записи
    assert FNAME == db.get_employee_info_max_id()[0][4]
    # список после добавления сотрудника
    body_after = apiE.get_a_list_of_employees(company_id)
    list_after = len(body_after)
    # сравнение списка и имени созданного сотрудника
    assert list_after - list_before == 1
    assert body_after[-1]['firstName'] == FNAME
    # *** удаляем сотрудника и потом БД из-за PM
    db.delete_employee(db_employee_id)
    db.delete_company(company_id)


""" Задание_3
проверка создать компанию и добавить сотрудника и получить по id
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


# проверка получить сотрудника по id
def test_get_employee_by_id():
    # получаем токен и создаем компанию
    token = apiC.get_an_authorization_token()
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = apiC.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # добавить сотрудника
    FNAME = 'Зомби'
    LNAME = 'Разлагайченко'
    user_response = apiE.add_a_new_employee(FNAME, LNAME, company_id, token)
    # берем id созданного сотрудника и запрашиваем его данные
    employee_id = user_response['id']
    response = apiE.get_employee_by_id(employee_id)
    # проверка полученных данных с api и с db
    assert response['id'] == employee_id == db.get_employee_info_max_id()[0][0]
    assert response['firstName'] == FNAME == db.get_employee_info_max_id()[0][4]
    # *** удаляем сотрудника и потом БД из-за PM
    db.delete_employee(db.get_employee_info_max_id()[0][0])
    db.delete_company(company_id)


""" Задание_4
проверка изменить информацию о сотруднике
ручные параметры: COMPANY_NAME, DESC, FNAME, LNAME
"""


def test_change_employee_information():
    # получаем токен и создаем компанию
    token = apiC.get_an_authorization_token()
    COMPANY_NAME = 'Мертвяки'
    DESC = 'У нас весело - присоединяйся'
    new_company_response = apiC.add_a_new_company(COMPANY_NAME, DESC, token)
    company_id = new_company_response['id']
    # добавить сотрудника
    FNAME = 'Зомби'
    LNAME = 'Разлагайченко'
    user_response = apiE.add_a_new_employee(FNAME, LNAME, company_id, token)
    employee_api_id = user_response['id']
    # получить пользователя и записать значения
    body_before = apiE.get_employee_by_id(employee_api_id)
    # изменить пользователя через API
    NEW_LNAME = 'Вампирский'
    NEW_EMAIL = 'vamp@gmail.com'
    apiE.change_employee_information(employee_api_id, NEW_LNAME, NEW_EMAIL, token)
    # получить измененного пользователя
    body_after = apiE.get_employee_by_id(employee_api_id)
    # сверить измененные данные
    assert body_before['id'] == body_after['id']
    assert body_after['lastName'] == NEW_LNAME
    assert body_before['lastName'] != body_after['lastName']
    assert body_before['email'] != body_after['email']
    # *** изменить пользователя через DB
    DB_NEW_LNAME = 'Zombovski'
    DB_NEW_EMAIL = 'Deadman@gmail.com'
    db.update_employee_data_by_id(employee_api_id, DB_NEW_LNAME, DB_NEW_EMAIL)

    employee_db_id = db.get_employee_info_by_id(employee_api_id)[0][0]
    employee_db_lname = db.get_employee_info_by_id(employee_api_id)[0][5]
    employee_db_email = db.get_employee_info_by_id(employee_api_id)[0][8]

    assert body_before['id'] == body_after['id'] == employee_db_id
    assert body_before['lastName'] != body_after['lastName'] != employee_db_lname
    assert db.get_employee_info_by_id(employee_api_id)[0][5] == DB_NEW_LNAME
    assert body_before['email'] != body_after['email'] != employee_db_email
    assert employee_db_email == DB_NEW_EMAIL
    
    db.delete_employee(employee_api_id)
    db.delete_company(company_id)
