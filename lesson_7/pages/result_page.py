class ResultPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    # Добавить все книги в корзину
    def add_books_in_the_cart(self):
        buy_buttons = self.driver.find_elements(
            "css selector", "a._btn.btn-tocart.buy-link"
            )
        count = 0
        for button in buy_buttons:
            button.click()
            count += 1
        return count

    def take_answer(self):
        search_field = self.driver.find_element(
            "xpath", "//div[@class='search-error bestsellers']"
            )
        return search_field.text
