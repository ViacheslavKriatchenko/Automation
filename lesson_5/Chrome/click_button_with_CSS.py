import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

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
