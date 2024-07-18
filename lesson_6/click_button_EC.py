from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Создание экземпляра вэбдрайвера
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1)

# Переход на вэб-страницу
URL = "http://uitestingplayground.com/ajax"
driver.get(URL)

# Ожидание загрузки страницы
wait.until(EC.url_to_be((URL)))

# Ожидание кликабельности кнопки и нажатие
AJAX_BUTTON = ("xpath", "//button[@id='ajaxButton']")
wait.until(EC.element_to_be_clickable((AJAX_BUTTON))).click()

# Ожидание появления элемента и изъятие текста
GREEN_FIELD = ("xpath", "//p[@class='bg-success']")
GREEN_FIELD_TEXT = wait.until(
    EC.visibility_of_element_located((GREEN_FIELD))
    ).text

# Вывод на печать информации
print(f'Текст поля - {GREEN_FIELD_TEXT}')
