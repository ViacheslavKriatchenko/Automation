class CartPage:

    def __init__(self, driver) -> None:
        self.driver = driver

    # Перейти в корзину
    def go_to_cart(self):
        self.driver.find_element(
            "xpath", "//a[contains(@class, 'cart-icon-js')]"
            ).click()

    # Получить количество товара в корзине
    def get_cart_count(self):
        cart_data = self.driver.find_element(
            "xpath", "//a[@data-event-label='myCart']/b"
            ).text
        return int(cart_data)
