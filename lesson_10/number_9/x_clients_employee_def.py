import requests


class EmployeeDef:
    def __init__(self, url) -> None:
        self.url = url

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
        response = requests.post(
            url=f'{self.url}employee',
            headers={
                'x-client-token': TOKEN
            },
            json=employee
        )
        return response.json()

    # функция получить сотрудника по id
    def get_employee_by_id(self, employee_id):
        response = requests.get(
            url=f'{self.url}employee/{employee_id}'
        )
        return response.json()

    # изменить информацию о сотруднике
    def change_employee_information(
            self, employee_id, new_lname, new_email, TOKEN
            ):
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
