class MainPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    # Открыть labirint.ru: https://www.labirint.ru/
    def open_labirint(self):
        self.driver.get("https://www.labirint.ru/")
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()

    # Найти все книги по слову
    def search_books(self, request):
        search_field = self.driver.find_element(
            "xpath", "//input[@id='search-field']"
            )
        search_field.send_keys(request)
        self.driver.find_element(
            "xpath", "//button[@type='submit']"
            ).click()
