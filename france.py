from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# URL france events (Will change to dynmaic endpoint)
url = "https://10times.com/france"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH) 
driver.get(url) 




# grabbing all event href and storing in list to iterate through, each page
events_france = []

time.sleep(5)
events = driver.find_element_by_xpath('//*[@id="listing-events"]')
event = [x for x in events.find_elements_by_tag_name("a")]

for eve in event:
    events_france.append(eve.get_attribute("href"))

driver.close()




print(events_france)




