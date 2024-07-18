from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1)
URL = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"

driver.get(URL)

SPINNER = ("xpath", "//span[@id='spinner']")
wait.until(EC.invisibility_of_element_located((SPINNER)))

THIRD_PICTURE = ("xpath", "(//div[@id='image-container']//img)[3]")
THIRD_PICTURE_DATA = driver.find_element(*THIRD_PICTURE).get_attribute("src")

print(f'Содержимое атрибута src - {THIRD_PICTURE_DATA}')
