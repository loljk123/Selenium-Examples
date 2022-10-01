from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "PATH"


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = (
    "Chrome Path"
)
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

driver.get("URL HERE")

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()


def waitPageLoad(secs: int, locator: By, text: str, driver: webdriver, click: bool):
    try:
        element = WebDriverWait(driver, secs).until(
            EC.presence_of_element_located((locator, text))
        )
        if click:
            element.click()
    except Exception:
        driver.quit()


waitPageLoad(10, By.LINK_TEXT, "TEXT HERE", driver, True)

waitPageLoad(10, By.ID, "ID HERE", driver, True)

driver.back()
driver.back()
driver.back()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
#     )
#     element.click()

# except:
#     driver.quit()
