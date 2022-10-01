from time import sleep

from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import os

#Above are imports required for things below ot work

if os.name == "nt":
    # windows
    PATH = "chromedriver.exe"
else:                 #OS CHECK FOR CHROMEDRIVER
    # linux/macos
    PATH = "./chromedriver"

BASE_URL = "ENTER URL HERE"
with open("config.json", "r") as f:         #reads a config.json to get any config variables that you might want. This can include class numbers or things like that. 
    config = json.load(f)
print("Starting Bot")
chrome_options = Options() # creates the default browser Options and stores it in the chrome_options variable
chrome_options.add_argument("user-data-dir=selenium") # saves cookies and the user profile to selenium directory
driver = uc.Chrome(PATH, chrome_options=chrome_options) # sets up the driver variable and we will use the driver variable from here on out. 
driver.get(BASE_URL)
print(driver.title) # prints the websites title to console so we can know which page we are at
driver.implicitly_wait(2) # waits 2 secodns
#Below here is where you would include any actions for the bot to do

driver.get(
    "ANOTHERURL"        # here the bot can go to another specified URL to to testing/automation on. 
)
driver.find_element(By.XPATH, '//*[@id="s2id_txt_term"]/a/span[2]/b').click()           # here the bot uses XPATH to find a specific element on the webpage


sleep(9999999999999999) # here we wait a large amount of time so we can do our own testing without the window closing. Useful for debugging. 
