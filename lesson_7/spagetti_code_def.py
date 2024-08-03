from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

"""
Написать тест:
Открыть labirint.ru: https://www.labirint.ru/.
Найти все книги по слову Python.
Добавить все книги в корзину.
Перейти в корзину.
Проверить, что счетчик товаров соответствует
количеству добавленных книг из шага c.
Упростить скрипт для чтения.
"""
options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)


# Открыть labirint.ru: https://www.labirint.ru/
def open_labirint():
    driver.get("https://www.labirint.ru/")
    cookie = {
        "name": "cookie_policy",
        "value": "1"
    }
    driver.add_cookie(cookie)
    driver.refresh()


# Найти все книги по слову Python
def search_books(request):
    search_field = driver.find_element("xpath", "//input[@id='search-field']")
    search_field.send_keys(request)
    driver.find_element("xpath", "//button[@type='submit']").click()


# Найти все книги по слову Python
def take_answer():
    search_field = driver.find_element(
        "xpath", "//div[@class='search-error bestsellers']"
        )
    assert "ничего не нашли" in search_field.text


# Добавить все книги в корзину
def add_books_in_the_cart():
    # all_searched_books_title = driver.find_elements(
    #     "xpath", "//div[@class='product-card need-watch watched gtm-watched']/a[@class='product-card__name']"
    #     )
    # count = 0
    # for book in all_searched_books_title:
    #     title_book = book.text
    #     count += 1
    #     print(f'{count} - {title_book}')
    buy_buttons = driver.find_elements(
        "css selector", "a._btn.btn-tocart.buy-link"
        )
    count = 0
    for button in buy_buttons:
        button.click()
        count += 1
    return count


# Перейти в корзину
def go_to_cart():
    driver.find_element(
        "xpath", "//a[contains(@class, 'cart-icon-js')]"
        ).click()


# Получить количество товара в корзине
def get_cart_count():
    cart_data = driver.find_element(
        "xpath", "//a[@data-event-label='myCart']/b"
        ).text
    return int(cart_data)


# Проверить, что счетчик соответствует количеству добавленных книг из шага 'C'
# def compare_values():
#     assert get_cart_count() == add_books_in_the_cart(), "количество не совпадает"
#     print("Все ОК!")


def close_browser():
    driver.quit()


# Тест Python
def test_labirint():
    open_labirint()
    search_books("Python")
    added = add_books_in_the_cart()
    print(added)
    go_to_cart()
    cart = get_cart_count()
    print(cart)
    close_browser()
    assert added == cart, "значения не совпадают"
    print("Всё ОК!")


# Тест пустой
def test_labirint_qqq():
    open_labirint()
    search_books("qqq")
    take_answer()
    close_browser()
    print("Всё ОК!")


# test_labirint()
test_labirint_qqq()
