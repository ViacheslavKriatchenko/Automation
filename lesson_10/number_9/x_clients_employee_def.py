import requests
import allure


class EmployeeDef:
    def __init__(self, url) -> None:
        self.url = url

    # функция получить список сотрудников компании
    @allure.step('API. Получить список сотрудников компании id = {company_id}')
    def get_a_list_of_employees(self, company_id: int) -> list:
        query_params = {
            'company': company_id
        }
        response = requests.get(
            url=f'{self.url}employee',
            params=query_params
        )
        return response.json()

    # функция добавить нового сотрудника
    @allure.step('API. Добавить нового сотрудника')
    def add_a_new_employee(
            self, fname: str, lname: str, companyID: int, TOKEN, isActive=True
            ) -> dict:
        employee = {
            "id": 0,
            "firstName": fname,
            "lastName": lname,
            "middleName": "",
            "companyId": companyID,
            "email": f'{fname}@gmail.com',
            "url": "",
            "phone": "",
            "birthdate": None,
            "isActive": isActive
        }
        response = requests.post(
            url=f'{self.url}employee',
            headers={
                'x-client-token': TOKEN
            },
            json=employee
        )
        return response.json()

    # функция получить сотрудника по id
    @allure.step('API. Получить сотрудника по id = {employee_id}')
    def get_employee_by_id(self, employee_id: int) -> dict:
        response = requests.get(
            url=f'{self.url}employee/{employee_id}'
        )
        return response.json()

    # изменить информацию о сотруднике
    @allure.step('API. Изменить информацию о сотруднике {employee_id}')
    def change_employee_information(
            self, employee_id: int, new_lname: str, new_email: str, TOKEN: str
            ) -> dict:
        response = requests.patch(
            url=f'{self.url}employee/{employee_id}',
            json={
                'lastName': new_lname,
                'email': new_email
            },
            headers={
                'x-client-token': TOKEN
            }
        )
        return response.json()
