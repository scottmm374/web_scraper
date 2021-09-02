from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# URL france events
url = "https://10times.com"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH) 
driver.get(url) 

# Issues with Exceptions thrown on button click (known issue with Chrome driver), so used this code to reach and activate button. 
driver.maximize_window()
btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
driver.execute_script("arguments[0].click();", btn)


# grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events
countries = []

time.sleep(7)
drop_down = driver.find_element_by_xpath('//*[@id="country"]')

options = [x for x in drop_down.find_elements_by_tag_name("option")]

for element in options:
    countries.append(element.get_attribute("value"))

driver.close()




print(len(countries))




