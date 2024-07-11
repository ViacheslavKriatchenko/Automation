from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
# firefox_options.add_argument("-incognito") - не работает в фоксе
# firefox_options.add_argument("-window-size=1980,1080") - не работает в фоксе
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = 'http://the-internet.herokuapp.com/entry_ad'

driver.get(url)

button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(('xpath', "//p[text()='Close']"))
    )
button.click()

driver.quit()
