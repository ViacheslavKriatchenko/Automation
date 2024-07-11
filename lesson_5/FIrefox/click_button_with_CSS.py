import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

chrome_options = webdriver.ChromeOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = 'http://uitestingplayground.com/classattr'

count = 0

for i in range(0, 3):
    driver.get(url)
    button_blue = driver.find_element(
        'xpath', "//button[contains(@class, 'btn-primary')]"
        )
    button_blue.click()
    count += 1
    print(count)
    time.sleep(2)
    driver.switch_to.alert.accept()

print(f'всего {count}')

driver.quit()
