import random
import time

import body
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys, actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

srv_obj = Service(r"C:\tools\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome()
driver.get('https://www.shopsy.in/')
driver.maximize_window()

#implicit wait
driver.implicitly_wait(10)
#actionchain
action = ActionChains(driver)

#explicit wait
wait = WebDriverWait(driver, 10)

#search product
search = driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
search.send_keys("tote bags women",Keys.ENTER)
time.sleep(2)

#open product
OpenProduct = driver.find_element(By.XPATH,"//div[3]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//img[1]")
driver.execute_script("arguments[0].scrollIntoView();", OpenProduct)
OpenProduct.click()
time.sleep(2)

#add to cart
AddToCart = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Add to cart')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", AddToCart)
driver.execute_script("arguments[0].click();", AddToCart)
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)

#search again
search = driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
search.send_keys("wallet for men",Keys.ENTER)
time.sleep(2)

#open wallet
wallet = driver.find_element(By.XPATH,"//div[@class='sc-46489703-1 drgEeC']//div[2]//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//img[1]")
driver.execute_script("arguments[0].scrollIntoView();", wallet)
wallet.click()

#wallet add to cart
AddToCart = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Add to cart')]"))
)
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", AddToCart)
driver.execute_script("arguments[0].click();", AddToCart)
time.sleep(2)

#logo
Logo = driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M9.946 13.')]")
Logo.click()
time.sleep(2)

#women
women = driver.find_element(By.XPATH,"//a[@href='/womens-clothing-online']//div[@class='sc-96001e20-2 hyPYQa']//img[@alt='cat nav image']")
action.move_to_element(women).perform()
time.sleep(1)

#men
men = driver.find_element(By.XPATH,"//a[@href='/mens-clothing-online']//div[@class='sc-96001e20-2 hyPYQa']//img[@alt='cat nav image']")
action.move_to_element(men).perform()
time.sleep(1)

#Gotocart
GoToCart = driver.find_element(By.XPATH,"//div[normalize-space()='Cart']")
GoToCart.click()
time.sleep(2)

#pincode
pin = driver.find_element(By.XPATH,"//div[contains(text(),'Enter Delivery Pincode')]")
pin.click()

#enter pin
Enter = driver.find_element(By.XPATH,"//input[@placeholder='Enter pincode']")
Enter.send_keys("123456")

#submit
Button = driver.find_element(By.XPATH,"//div[contains(text(),'Submit')]").click()
time.sleep(2)

driver.close()



