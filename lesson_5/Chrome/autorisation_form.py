import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://the-internet.herokuapp.com/login'

driver.get(url)

username_field = driver.find_element('xpath', "//input[@id='username']")
username_field.send_keys('tomsmith')
time.sleep(2)

password_field = driver.find_element('xpath', "//input[@id='password']")
password_field.send_keys('SuperSecretPassword!')
time.sleep(2)

submit_button = driver.find_element('xpath', "//button[@type='submit']")
submit_button.click()
time.sleep(2)
