import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

url = 'http://the-internet.herokuapp.com/add_remove_elements/'

driver.get(url)

button_add_element = driver.find_element(
    'xpath', "//button[contains(text(), 'Add Element')]"
    )

time.sleep(2)
for i in range(0, 5):
    button_add_element.click()
    time.sleep(2)

button_delete = driver.find_elements(
    'xpath', "//button[contains(text(), 'Delete')]"
    )

print(f'Размер списка кнопок Delete = {len(button_delete)}')

driver.quit()
