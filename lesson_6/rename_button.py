from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# Создание экземпляра вэбдрайвера
options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=0.5)

# Переход на вэб-страницу
URL = "http://uitestingplayground.com/textinput"
driver.get(URL)

# Ввод текста в поле
INPUT_FIELD = ("xpath", "//input[@id='newButtonName']")
driver.find_element(*INPUT_FIELD).send_keys("SkyPro")

# Ожидание кликабельности кнопки и нажатие
BLUE_BUTTON = ("xpath", "//button[@id='updatingButton']")
wait.until(EC.element_to_be_clickable((BLUE_BUTTON))).click()

# Ожидание появления элемента и изъятие текста
BLUE_BUTTON_TEXT = wait.until(
     EC.visibility_of_element_located((BLUE_BUTTON))
    ).text

# Вывод на печать информации
print(f'Текст кнопки - {BLUE_BUTTON_TEXT}')
