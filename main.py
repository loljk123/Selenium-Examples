from time import sleep

from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import os

if os.name == "nt":
    # windows
    PATH = "chromedriver.exe"
else:                 #OS CHECK FOR CHROMEDRIVER
    # linux/macos
    PATH = "./chromedriver"

BASE_URL = "ENTER URL HERE"
with open("config.json", "r") as f:
    config = json.load(f)
print("Starting Bot")
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") # saves cookies and the user profile to selenium directory
driver = uc.Chrome(PATH, chrome_options=chrome_options)
driver.get(BASE_URL)
print(driver.title)
driver.implicitly_wait(2)
#Below here is where you would include any login to login

driver.get(
    "ANOTHERURL"
)
driver.find_element(By.XPATH, '//*[@id="s2id_txt_term"]/a/span[2]/b').click()


sleep(9999999999999999)
