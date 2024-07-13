import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://the-internet.herokuapp.com/inputs'

driver.get(url)

input_field = driver.find_element('xpath', "//input[@type='number']")
input_field.send_keys('1000')
time.sleep(3)

input_field.clear()
time.sleep(3)

input_field.send_keys('999')
time.sleep(3)
