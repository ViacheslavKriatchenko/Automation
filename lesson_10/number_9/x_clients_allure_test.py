from x_clients_company_def import CompanyDef
from x_clients_employee_def import EmployeeDef
from x_clients_db_def import DbTable
from data import Data
import allure


@allure.epic('Приложение X-Clients')
@allure.title('Тестирование приложения X-Clients')
@allure.description('Тестирование API и БД приложения')
@allure.feature('Компании и сотрудники')
@allure.link('https://x-clients-be.onrender.com/', name='X-Clients')
@allure.severity(allure.severity_level.CRITICAL)
@allure.issue("X-Clients-1")
class TestEmployee:

    BASE_URL = "https://x-clients-be.onrender.com/"
    db_connection_path = (
        "postgresql://x_clients_user:"
        "95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@"
        "dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/"
        "x_clients_db_fxd0"
    )

    apiC = CompanyDef(BASE_URL)
    apiE = EmployeeDef(BASE_URL)
    db = DbTable(db_connection_path)
    env = Data()

    @allure.story("Получение токена")
    def test_get_an_authorization_token(self):
        with allure.step("Отправить API запрос на получение токена"):
            TOKEN = self.apiC.get_an_authorization_token()
        print(TOKEN)
        with allure.step("Проверить что переменная токен не пустая"):
            assert TOKEN is not None

    @allure.story("Получить список сотрудников компании")
    @allure.testcase("Emp-1")
    def test_get_a_list_of_employees(self):

        # получить токен
        token = self.apiC.get_an_authorization_token()

        with allure.step('Получение списков компаний до внесения изменений'):
            before_all_companies_response = self.apiC.get_list_companies()
            before_all_companies_response_db = self.db.get_all_companies()

        # создать компанию
        self.apiC.add_a_new_company(
            self.env.COMPANY_NAME, self.env.DESC, token
            )

        # получить список компаний после добавления
        after_all_companies_response = self.apiC.get_list_companies()

        # записываем в переменную id созданной компании
        company_id = after_all_companies_response[-1]["id"]
        data = self.apiE.get_a_list_of_employees(company_id)

        with allure.step('Удаление созданной компании из БД'):
            self.db.delete_company(company_id)

        with allure.step('Сравнение длины списка БД и API'):
            assert len(before_all_companies_response) == len(
                before_all_companies_response_db
            )

        with allure.step('Сравнение данных'):
            assert (
                len(after_all_companies_response) - len(before_all_companies_response) == 1
            )
            assert after_all_companies_response[-1]["name"] == self.env.COMPANY_NAME
            # проверяем что возвращается список сотрудников
            assert isinstance(data, list) is True

    @allure.story("Добавить нового сотрудника компании")
    @allure.testcase("Emp-2")
    def test_add_a_new_employee(self):

        # получаем токен и создаем компанию
        token = self.apiC.get_an_authorization_token()
        new_company_response = self.apiC.add_a_new_company(
            self.env.COMPANY_NAME, self.env.DESC, token
            )
        company_id = new_company_response["id"]

        with allure.step('Проверяем что в базе создалась компания и id равны'):
            assert company_id == self.db.get_max_company_id()[0][0]

        with allure.step('Создаем переменные до добавления сотрудника'):
            body_before = self.apiE.get_a_list_of_employees(company_id)
            list_before = len(body_before)

        with allure.step('Добавляем нового сотрудника'):
            self.apiE.add_a_new_employee(self.env.FNAME, self.env.LNAME, company_id, token)
            db_employee_id = self.db.get_employee_info_max_id()[0][0]

        with allure.step('Сравниваем введенное имя с именем в БД'):
            assert self.env.FNAME == self.db.get_employee_info_max_id()[0][4]

        with allure.step('Создаем переменные после добавления сотрудника'):
            body_after = self.apiE.get_a_list_of_employees(company_id)
            list_after = len(body_after)

        with allure.step('Сравнение списка и имени созданного сотрудника'):
            assert list_after - list_before == 1
            assert body_after[-1]["firstName"] == self.env.FNAME

        with allure.step('Удаление созданной информации из БД'):
            self.db.delete_employee(db_employee_id)
            self.db.delete_company(company_id)

    @allure.story("Получить сотрудника по id")
    @allure.testcase("Emp-3")
    def test_get_employee_by_id(self):

        token = self.apiC.get_an_authorization_token()
        new_company_response = self.apiC.add_a_new_company(
            self.env.COMPANY_NAME, self.env.DESC, token
            )
        company_id = new_company_response["id"]

        # добавить сотрудника
        user_response = self.apiE.add_a_new_employee(
            self.env.FNAME, self.env.LNAME, company_id, token
            )

        with allure.step('Присваиваем переменной id созданного сотрудника'):
            employee_id = user_response["id"]
        response = self.apiE.get_employee_by_id(employee_id)

        with allure.step('Сверяем данные API и БД'):
            assert response["id"] == employee_id == self.db.get_employee_info_max_id()[0][0]
            assert response["firstName"] == self.env.FNAME == self.db.get_employee_info_max_id()[0][4]

        with allure.step('Удаление созданной информации из БД'):
            self.db.delete_employee(self.db.get_employee_info_max_id()[0][0])
            self.db.delete_company(company_id)

    @allure.story("Изменить информацию о сотруднике")
    @allure.testcase("Emp-4")
    def test_change_employee_information(self):
        # получаем токен и создаем компанию
        token = self.apiC.get_an_authorization_token()
        new_company_response = self.apiC.add_a_new_company(
            self.env.COMPANY_NAME, self.env.DESC, token
            )
        company_id = new_company_response["id"]

        # добавить сотрудника
        user_response = self.apiE.add_a_new_employee(
            self.env.FNAME, self.env.LNAME, company_id, token
            )
        employee_api_id = user_response["id"]

        # получить пользователя и записать значения
        body_before = self.apiE.get_employee_by_id(employee_api_id)

        # изменить пользователя через API
        self.apiE.change_employee_information(
            employee_api_id, self.env.NEW_LNAME, self.env.NEW_EMAIL, token
        )

        # получить измененного пользователя
        body_after = self.apiE.get_employee_by_id(employee_api_id)

        # сверить измененные данные
        with allure.step('Проверяем данные на изменение'):
            assert body_before["id"] == body_after["id"]
            assert body_after["lastName"] == self.env.NEW_LNAME
            assert body_before["lastName"] != body_after["lastName"]
            assert body_before["email"] != body_after["email"]

        # *** изменить пользователя через DB
        self.db.update_employee_data_by_id(
            employee_api_id, self.env.DB_NEW_LNAME, self.env.DB_NEW_EMAIL
        )

        employee_db_id = self.db.get_employee_info_by_id(employee_api_id)[0][0]
        employee_db_lname = self.db.get_employee_info_by_id(employee_api_id)[0][5]
        employee_db_email = self.db.get_employee_info_by_id(employee_api_id)[0][8]

        with allure.step(
            'Проверяем что id созданного сотрудника'
            'не меняется после обновления через API и БД'
        ):
            assert body_before["id"] == body_after["id"] == employee_db_id

        with allure.step(
            'Проверяем что имя сотрудника'
            'меняется после обновлений'
        ):
            assert body_before["lastName"] != body_after["lastName"] != employee_db_lname

        with allure.step('Имя в БД равно введенному'):
            assert self.db.get_employee_info_by_id(employee_api_id)[0][5] == self.env.DB_NEW_LNAME

        with allure.step('Проверяем что данные почты меняются после обновления'):
            assert body_before["email"] != body_after["email"] != employee_db_email

        with allure.step('Почта в БД равна введенной'):
            assert employee_db_email == self.env.DB_NEW_EMAIL

        with allure.step('Удаление созданной информации из БД'):
            self.db.delete_employee(employee_api_id)
            self.db.delete_company(company_id)
