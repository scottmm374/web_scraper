from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import env
import random
import mimic


# chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('start-maximized')
# chrome_options.add_argument('--disable-notifications')

# x = random.randint(4,60)
# URL france events
URL = "https://10times.com"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH, options=chrome_options) 
random_sleep = random.randint(4,300)
sleep = round((random_sleep / 7), 4)


# Issues with Exceptions thrown on button click (known issue with Chrome driver), so used this code to reach and activate button. 
country_url = []
countries = []



driver.get(URL) 

driver.maximize_window()
time.sleep(sleep)
# Login
try:
    login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')

    print('found login')
    driver.execute_script("arguments[0].click();", login_link)
except:
    print('Cant find Login')
    driver.close()
    driver.quit()

time.sleep(sleep)


try:
    login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
    print('found email')
    login_email.send_keys(env.EMAIL)
except:
    print('Cant find email')
    driver.quit()
time.sleep(sleep)

# agreement button

try:
    check_box = driver.find_element_by_xpath('//*[@id="i2"]')
    print('checkbox')
    driver.execute_script("arguments[0].click();", check_box)
except:
    print('Cant find checkbox')
    driver.quit()
time.sleep(sleep)



try:
    next_btn = driver.find_element_by_xpath('//*[@id="send"]')
    print('next')
    driver.execute_script("arguments[0].click();", next_btn)

except:
    print('Cant find next')
    driver.quit()
time.sleep(sleep)


try:
    enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
    print('found pswd')
    enter_pswd.send_keys(env.PSWD)
except:
    print('pswd not found')
    driver.quit()

time.sleep(sleep * 2)


try:
    pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
    print('found pswd next')
    driver.execute_script("arguments[0].click();", pswd_next_btn)

except:
    print('pswd next not found')
    driver.quit()


time.sleep(sleep)


# def countries():  
# Grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events


try:
    btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
    driver.execute_script("arguments[0].click();", btn)

except:
    driver.quit()

try:

    drop_down = driver.find_element_by_xpath('//*[@id="country"]')
    options = [x for x in drop_down.find_elements_by_tag_name("option")]

except:
    driver.quit()



for element in options:

    countries.append(element.get_attribute("value"))
    

# for country in range(len(countries)):
#     country_url = 'https://10times.com' + countries[country]
#     country_url.append(country_url)
# print(country_url)
with open('countries.txt', 'w') as file:
    try:
        for country in countries:
            file.write(f'https://10times.com{country}')
            file.write('\n')
    except:
        driver.close()
        driver.quit()   

# print(countries)
driver.close()
driver.quit() 








    









