from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.options import Options

# chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-popup-blocking')
# chrome_options.add_argument('start-maximized')


# URL france events (Will change to dynmaic endpoint)
url = "https://10times.com/france"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH) 
driver.get(url) 
time.sleep(7)

# login

# search_username_by_id = driver.find_element_by_id('//*[@id="userEmail"]')
# search_username_by_id.send_keys("scottmichelle74@gmail.com")

# /html/body/div[8]/div/div/div/div[2]/div/form/div[2]/svg  xpath to accept button

# input password
# search_password_by_id = driver.find_element_by_id("password")
# search_password_by_id.send_keys("") # remove senstive data to push code until encrytiopn can be set up

# execute the login button
# login_button = driver.find_element_by_id("fs-login-button")
# login_button.send_keys(Keys.RETURN)
# Navigate to the ticker symbol A

# driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)

# Scroll works but not completly as of yet.
ScrollNumber = 50
for i in range(1, ScrollNumber):
    time.sleep(5)
    driver.execute_script('window.scrollTo(1,50000)')
    time.sleep(5)

# grabbing all event href and storing in list to iterate through, each page
events_france = []

time.sleep(3)
events = driver.find_element_by_xpath('//*[@id="listing-events"]')
event = [x for x in events.find_elements_by_tag_name("a")]

for eve in event:
    events_france.append(eve.get_attribute("href"))

driver.close()


# Next step figure out a proper data structure (Dictionary (key = event name) with list of information as value?), or convert into csv instead?

print(len(events_france))




