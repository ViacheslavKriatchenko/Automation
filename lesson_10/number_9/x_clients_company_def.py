import requests


class CompanyDef:

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

    # функция добавить новую компанию
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
