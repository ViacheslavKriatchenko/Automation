from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1)
URL = "http://uitestingplayground.com/ajax"

driver.get(URL)

wait.until(EC.url_to_be((URL)))

AJAX_BUTTON = ("xpath", "//button[@id='ajaxButton']")
wait.until(EC.element_to_be_clickable((AJAX_BUTTON))).click()

GREEN_FIELD = ("xpath", "//p[@class='bg-success']")
GREEN_FIELD_TEXT = wait.until(
    EC.visibility_of_element_located((GREEN_FIELD))
    ).text

print(f'Текст поля - {GREEN_FIELD_TEXT}')
