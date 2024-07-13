import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless") - запустить без развертывания
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://the-internet.herokuapp.com/add_remove_elements/'

driver.get(url)

button_add_element = driver.find_element(
    'xpath', "//button[contains(text(), 'Add Element')]"
    )

time.sleep(2)
for i in range(0, 5):
    button_add_element.click()
    time.sleep(3)

button_delete = driver.find_elements(
    'xpath', "//button[contains(text(), 'Delete')]"
    )

print(f'Размер списка кнопок Delete = {len(button_delete)}')
