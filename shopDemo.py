from importlib.metadata import pass_none
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

service = Service(r"C:\tools\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
driver.get("https://www.onlineshopdemo.co.uk/")
driver.maximize_window()
time.sleep(5)

actions = ActionChains(driver)

body = driver.find_element(By.TAG_NAME, "body")
#scroll
Last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(0.5, 2))

    New_height = driver.execute_script("return document.body.scrollHeight")
    if New_height == Last_height:
        count +=1
        if count == 6:
            break
    else:
        count =0
        Last_height = New_height


#scroll up
Last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
while True:
    body.send_keys(Keys.PAGE_UP)
    time.sleep(random.uniform(0.5, 2))

    New_height = driver.execute_script("return document.body.scrollHeight")
    if New_height == Last_height:
        count +=1
        if count == 6:
            break
    else:
        count =0
        Last_height = New_height

#search
search = driver.find_element(By.XPATH, "//div[@class='jet-popup-target elementor-element elementor-element-8e4d943 elementor-widget__width-auto elementor-view-default elementor-widget elementor-widget-icon jet-popup-attach-event-inited jet-popup-cursor-pointer']//a[@class='elementor-icon']//*[name()='svg']")
search.click()
time.sleep(2)
#searchforanything
SearchFor = driver.find_element(By.XPATH, "//input[@placeholder='Search this store']")
SearchFor.send_keys("sweater",Keys.ENTER)

#open
target_xpath = "//li[@class='jet-woo-builder-product jet-woo-builder-archive-item-8611 jet-woo-thumb-with-effect product type-product post-8611 status-publish last instock product_cat-womens-collections product_tag-woman-jumpers-and-sweaters has-post-thumbnail shipping-taxable purchasable product-type-variable']//a[@aria-label='Select options for “100% cashmere sweater”'][normalize-space()='Select options']"

while True:
    try:
        product = driver.find_element(By.XPATH, target_xpath)

        if product.is_displayed():
            print(" product 1")
            break

    except:
        pass

    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(random.uniform(0.5, 1.5))

# after loop
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", product)

product = wait.until(
    EC.element_to_be_clickable((By.XPATH, target_xpath))
)
product.click()

#open color
clr = Select(driver.find_element(By.XPATH,"//select[@id='pa_color']"))
clr.select_by_visible_text("Heather Grey")

#size
op_size = Select(driver.find_element(By.XPATH, "//select[@id='pa_size']"))
op_size.select_by_visible_text("XS")
time.sleep(2)

#add to cart
btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']")
driver.execute_script("arguments[0].scrollIntoView();", btn)
btn.click()
time.sleep(2)

#home
Home = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M280.37 14')]")
Home.click()
time.sleep(2)

#hover on cart
cart = driver.find_element(By.XPATH,"//div[@class='elementor-element elementor-element-b74a284 elementor-widget__width-auto elementor-widget elementor-widget-jet-blocks-cart']")
actions.move_to_element(cart).perform()
time.sleep(2)
driver.quit()