import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

chrome_options = webdriver.ChromeOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = 'http://the-internet.herokuapp.com/inputs'

driver.get(url)

input_field = driver.find_element('xpath', "//input[@type='number']")
input_field.send_keys('1000')
time.sleep(3)

input_field.clear()
time.sleep(3)

input_field.send_keys('999')
time.sleep(3)

driver.quit()
