import random
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

serv_ob= Service(r"C:\tools\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_ob)
driver.get("https://www.nykaa.com/")
driver.maximize_window()
time.sleep(5)

#action chain
actions = ActionChains(driver)

#explicit wait
wait = WebDriverWait(driver, 10)

body = driver.find_element(By.TAG_NAME, "body")
#scroll down
last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(1,2))
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        count += 1
        if count == 7 :
            break
    else:
        count = 0
        last_height = new_height

#scroll up
up = driver.find_element(By.XPATH,"//button[@aria-label='Back to Top']//*[name()='svg']")
up.click()
time.sleep(2)

#hover on header
categories = driver.find_element(By.ID, "category")
actions.move_to_element(categories).perform()

brands = driver.find_element(By.XPATH,"//a[normalize-space()='brands']")
actions.move_to_element(brands).perform()

luxe = driver.find_element(By.XPATH,"//a[normalize-space()='luxe']")
actions.move_to_element(luxe).perform()

nykaFeshion = driver.find_element(By.XPATH,"//a[@href='/'][normalize-space()='Nykaa Fashion']")
actions.move_to_element(nykaFeshion).perform()

beauty = driver.find_element(By.XPATH,"//a[normalize-space()='Beauty Advice']")
actions.move_to_element(beauty).perform()

#search
search = driver.find_element(By.XPATH,"//input[@placeholder='Search on Nykaa']")
search.send_keys("make up brush",Keys.ENTER)

#main tab
main_tab = driver.current_window_handle

# open
brush = None

for _ in range(10):
    try:
        brush = driver.find_element(By.XPATH,"//img[@alt='Bronson Professional 4 in 1 Travel Brush Foundation Brush, Powder Brush, Eyeshadow Brush, Flat Brush']")

        if brush.is_displayed():
            break
    except:
        pass

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.3)

# after loop
if brush:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", brush)
    brush.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
else:
    print(" Element not found")

time.sleep(5)

#add to bag
btn = driver.find_element(By.XPATH,"//div[@class='css-vp18r8']//button[@type='button']")
btn.click()
time.sleep(2)

#close brush tab
driver.close()
driver.switch_to.window(main_tab)
time.sleep(2)

#back
driver.back()
time.sleep(2)

#mac
for _ in range(5):
    mac = driver.find_elements(By.XPATH,"//div[@id='69d64f4f0eceff8ae4ccaf8a']//div[@class='callout-radius css-xb5jjx']")
    if mac and mac[0].is_displayed():
        driver.execute_script("arguments[0].click();", mac[0])
        break

    else:
        arrow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1w3it08']//div//div[@class='css-1ojspo7']"))
        )
        arrow.click()
        time.sleep(1)

#open foundation
foundation = None

for _ in range(10):
    try:
        foundation = driver.find_element(By.XPATH,"//img[@alt='M.A.C Studio Fix Fluid SPF 15 Soft Matte Foundation With Hyaluronic Acid - C40']")

        if foundation.is_displayed():
            break
    except:
        pass

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.3)

# after loop
if foundation:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",foundation)
    foundation.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
else:
    print(" Element not found")

time.sleep(5)

#close popup
body = driver.find_element(By.TAG_NAME,"body")
body.click()

#scroll down
last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(1,2))
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        count += 1
        if count == 7 :
            break
    else:
        count = 0
        last_height = new_height

#scroll up
up = driver.find_element(By.XPATH,"//button[@aria-label='Back to Top']//*[name()='svg']")
up.click()
time.sleep(2)

#close foundation tab
driver.close()
driver.switch_to.window(main_tab)
time.sleep(2)

driver.back()
time.sleep(2)

#explore all brands
exp_brand = None

for _ in range(10):
    try:
        exp_brand = driver.find_element(By.XPATH,"//img[@alt='PZN_COH_PremiumExp_UltraLuxe_Best of Luxury View All']")

        if exp_brand.is_displayed():
            break
    except:
        pass

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.3)

# after loop
if brush:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", exp_brand)
    exp_brand.click()
    time.sleep(2)

#scroll down
last_height = driver.execute_script("return document.body.scrollHeight")

count = 0
while True:
    body = driver.find_element(By.TAG_NAME,"body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(random.uniform(1,2))
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        count += 1
        if count == 7 :
            break
    else:
        count = 0
        last_height = new_height

#scroll up
up = driver.find_element(By.XPATH,"//button[@aria-label='Back to Top']//*[name()='svg']")
up.click()
time.sleep(2)

driver.back()

#cart
cart = driver.find_element(By.XPATH,"//div[@class='css-0 e1ewpqpu1']")
cart.click()
time.sleep(2)

#delete product
delete = driver.find_element(By.XPATH,"//button[@aria-label='delete']//*[name()='svg']")
delete.click()
time.sleep(2)

#yes
yes = driver.find_element(By.XPATH,"//button[normalize-space()='Yes']")
yes.click()
time.sleep(2)

#back
back_Cart = driver.find_element(By.XPATH,"//div[@aria-label='Back']//*[name()='svg']")
back_Cart.click()
time.sleep(2)

#more
more = None

for _ in range(10):
    try:
        more = driver.find_element(By.XPATH,"//img[@alt='2734']")

        if more.is_displayed():
            break
    except:
        pass

    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(0.3)

# after loop
if more:
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", more)
    more.click()
    time.sleep(2)

driver.back()
time.sleep(2)

#scroll up
up = driver.find_element(By.XPATH,"//button[@aria-label='Back to Top']//*[name()='svg']")
up.click()
time.sleep(2)

#sub header
make_up = driver.find_element(By.XPATH,"//a[@role='menuitem'][normalize-space()='makeup']")
actions.move_to_element(make_up).perform()
time.sleep(2)

skin = driver.find_element(By.XPATH,"//a[@role='menuitem'][normalize-space()='skin']")
actions.move_to_element(skin).perform()
time.sleep(2)

hair = driver.find_element(By.XPATH,"//a[normalize-space()='hair']")
actions.move_to_element(hair).perform()
time.sleep(2)

driver.quit()
