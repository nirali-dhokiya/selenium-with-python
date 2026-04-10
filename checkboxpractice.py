import time
from re import search

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait

serv_obj = Service(r"C:\tools\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#driver.implicitly_wait(10)

checkboxes = driver.find_elements (By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
driver.execute_script("arguments[0].scrollIntoView();", checkboxes[0])

#select multiple checkbox by choice
# for checkbox in checkboxes:
  #  weekname = checkbox.get_attribute('id')
   # if weekname == 'monday' or weekname == 'tuesday':
    #    checkbox.click()

#SELECT LAST 2 CHECKBOX
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
time.sleep(5)

#SELECT first 2 CHECKBOX
for i in range(len(checkboxes)):
    if i<2:
       checkboxes[i].click()
time.sleep(5)



#checkbox = driver.find_element(By.XPATH, "//input[@id='monday']")
#driver.execute_script("arguments[0].scrollIntoView();", checkbox)
#checkbox.click()
#time.sleep(2)


#for checkbox in checkboxes:
 #   checkbox.click()

driver.quit()

