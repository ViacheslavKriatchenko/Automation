import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

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

driver.quit()
