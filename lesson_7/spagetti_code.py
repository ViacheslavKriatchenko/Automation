from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from time import sleep
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
driver.get("https://www.labirint.ru/")
cookie = {
    "name": "cookie_policy",
    "value": "1"
}
driver.add_cookie(cookie)
driver.refresh()
# Найти все книги по слову Python
search_field = driver.find_element("xpath", "//input[@id='search-field']")
search_field.send_keys("Python")
driver.find_element("xpath", "//button[@type='submit']").click()
# Добавить все книги в корзину
all_searched_books_title = driver.find_elements(
    "xpath", "//div[@class='product-card need-watch watched gtm-watched']/a[@class='product-card__name']"
    )
count = 0
for book in all_searched_books_title:
    title_book = book.text
    count += 1
    print(f'{count} - {title_book}')

buy_buttons = driver.find_elements("css selector", "a._btn.btn-tocart.buy-link")
for button in buy_buttons:
    button.click()
sleep(3)
# Перейти в корзину
driver.find_element("xpath", "//a[contains(@class, 'cart-icon-js')]").click()
sleep(3)
# Проверить, что счетчик товаров соответствует
# количеству добавленных книг из шага 'C'
cart_count = driver.find_element(
    "xpath", "//a[@data-event-label='myCart']/b"
    ).text
assert int(cart_count) == count, "количество не совпадает"
print("Все ОК!")

driver.quit()
