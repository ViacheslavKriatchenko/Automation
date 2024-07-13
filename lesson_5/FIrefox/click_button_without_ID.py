import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

chrome_options = webdriver.ChromeOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = 'http://uitestingplayground.com/dynamicid'

count = 0

for i in range(0, 3):
    driver.get(url)
    button_with_Dynamic_ID = driver.find_element(
        'xpath', "//div//button[contains(@class, 'btn') and @type='button']"
        )
    button_with_Dynamic_ID.click()
    count += 1
    print(count)
    time.sleep(2)

print(f'всего {count}')
driver.quit()
