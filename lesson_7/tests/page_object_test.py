from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lesson_7.pages.cart_page import CartPage
from lesson_7.pages.main_page import MainPage
from lesson_7.pages.result_page import ResultPage


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")  # без браузера
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)


def test_cart_count_with_argument():

    main = MainPage(driver)
    main.open_labirint()
    main.search_books("Python")

    result = ResultPage(driver)
    added = result.add_books_in_the_cart()

    cart = CartPage(driver)
    cart.go_to_cart()
    have = cart.get_cart_count()

    assert added == have, "числа не совпали"

    driver.quit()


def test_cart_count_wrong_argument():

    main = MainPage(driver)
    main.open_labirint()
    main.search_books("qqq")

    result = ResultPage(driver)
    answer = result.take_answer()

    assert "ничего не нашли" in answer

    driver.quit()
