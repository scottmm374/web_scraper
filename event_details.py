from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import csv

from selenium.webdriver.chrome.options import Options
# chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')

random_sleep = random.randint(4,100)
sleeping = round((random_sleep / 7), 4)
print(sleeping)
# URL france events

# URL france events (Will change to dynmaic endpoint)
france_url = "https://10times.com/le-cuir-a-paris"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH, options=chrome_options) 
driver.get(france_url) 
driver.maximize_window()
sleep(10)


titles = []
event_single = []


# Grabs all text elements in table, have to clean up data.
timings = driver.find_element_by_xpath('//*[@id="content"]/section[3]/table')

text = [timings.get_attribute('innerText').replace('\n', ',')]


# Gets the description
desc = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/section[1]/p').text
print(desc)

# print(text)

   
driver.close()
driver.quit()









    
    