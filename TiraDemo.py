import random
import time

import body
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service(r"C:\tools\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
wait = WebDriverWait(driver, 10)

#open tira
driver.get("https://www.tirabeauty.com/")
driver.maximize_window()
time.sleep(2)

body = driver.find_element(By.TAG_NAME, "body")

#human scroll using page down until site end
Last_Height = driver.execute_script("return document.body.scrollHeight")

while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(0.5, 2))

    New_Height = driver.execute_script("return document.body.scrollHeight")

    #stop
    if New_Height == Last_Height:
        break
        Last_Height = New_Height

#advance version
count = 0
while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(0.5, 2))
    New_Height = driver.execute_script("return document.body.scrollHeight")

    if New_Height == Last_Height:
        count += 1
        if count ==3:
            break
    else:
        count = 0
        Last_Height = New_Height

#human scrolling in loop
for _ in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(0.5, 2))

