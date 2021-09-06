from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import env
import random
# chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-notifications')

x = random.randint(4,20)
# URL france events
url = "https://10times.com"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH, options=chrome_options) 


driver.get(url) 

# Issues with Exceptions thrown on button click (known issue with Chrome driver), so used this code to reach and activate button. 
driver.maximize_window()
time.sleep(7)


# Login
# login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')
try:
    login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')

    print('found login')
    driver.execute_script("arguments[0].click();", login_link)
except:
    print('Cant find Login')
    driver.close()
    driver.quit()

time.sleep(x)


try:
    login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
    time.sleep(x)
    print('found email')
    login_email.send_keys(env.EMAIL)
except:
    print('Cant find email')
    driver.quit()
time.sleep(x)

# agreement button

try:
    check_box = driver.find_element_by_xpath('//*[@id="i2"]')
    print('checkbox')
    driver.execute_script("arguments[0].click();", check_box)
except:
    print('Cant find checkbox')
    driver.quit()
time.sleep(x)



try:
    next_btn = driver.find_element_by_xpath('//*[@id="send"]')
    print('next')
    driver.execute_script("arguments[0].click();", next_btn)

except:
    print('Cant find next')
    driver.quit()
time.sleep(x)


try:
    enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
    print('found pswd')
    enter_pswd.send_keys(env.PSWD)
except:
    print('pswd not found')
    driver.quit()

time.sleep(x)


try:
    pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
    print('found pswd next')
    driver.execute_script("arguments[0].click();", pswd_next_btn)
   
except:
    print('pswd next not found')
    driver.quit()

driver.close()    
driver.quit()

# print('We reached the end')

time.sleep(x)

# btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
# driver.execute_script("arguments[0].click();", btn)






# grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events
countries = []

time.sleep(7)
drop_down = driver.find_element_by_xpath('//*[@id="country"]')

options = [x for x in drop_down.find_elements_by_tag_name("option")]

for element in options:
    countries.append(element.get_attribute("value"))

driver.close()




print(countries)

driver.quit()

