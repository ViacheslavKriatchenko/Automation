class Smartphone:

    def __init__(self, brand: str, model: str, number: str) -> None:
        self.brand: str = brand
        self.model: str = model
        self.number: str = number
        assert number[:3] == '+79', 'неверный код номера'


# тест assert
# phone_1 = Smartphone('samsung', 'a52', '+76456230')
# phone_2 = Smartphone('samsung', 'a52', '+79456230')
