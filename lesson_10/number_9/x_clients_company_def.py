import requests
import allure


class CompanyDef:

    def __init__(self, url) -> None:
        self.url = url

    # функция получить список компаний
    @allure.step('API. Получить список всех компаний')
    def get_list_companies(self) -> list:
        response = requests.get(
            url=f'{self.url}company'
        )
        return response.json()

    # функция получить токен авторизации
    @allure.step('API. Получить токен авторизации для {name}:{password}')
    def get_an_authorization_token(
            self, name: str = 'donatello', password: str = 'does-machines'
            ) -> str:
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
    @allure.step('API. Добавить новую компанию')
    def add_a_new_company(
            self, company_name: str, desc: str, TOKEN: str
            ) -> dict:
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
