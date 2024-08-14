import requests


class EmployeeDef:

    def __init__(self, url) -> None:
        self.url = url

    # функция получить список компаний
    def get_list_companies(self):
        response = requests.get(
            url=f'{self.url}company'
        )
        return response.json()

    # функция получить токен авторизации
    def get_an_authorization_token(
            self, name='donatello', password='does-machines'
            ):
        response = requests.post(
            url=f'{self.url}auth/login',
            json={
                'username': name,
                'password': password
            }
        )
        TOKEN = response.json()['userToken']
        return TOKEN

    # функция получить список сотрудников компании
    def get_a_list_of_employees(self, company_id: int):
        query_params = {
            'company': company_id
        }
        response = requests.get(
            url=f'{self.url}employee',
            params=query_params
        )
        return response.json()

    # функция добавить нового сотрудника
    def add_a_new_employee(
            self, fname: str, lname: str, companyID: int, TOKEN, isActive=True
            ):
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
        requests.post(
            url=f'{self.url}employee',
            headers={
                'x-client-token': TOKEN
            },
            json=employee
        )

    # функция получить сотрудника по id
    def get_employee_by_id(self, employee_id):
        response = requests.get(
            url=f'{self.url}employee/{employee_id}'
        )
        return response.json()

    # изменить информацию о сотруднике
    def change_employee_information(self, employee_id, new_lname, new_email, TOKEN):
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
