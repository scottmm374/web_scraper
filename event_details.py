from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import csv
import env


# chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')

random_sleep = random.randint(4,100)
sleeping = round((random_sleep / 7), 4)
print(sleeping)


# URL france events (Will change to dynmaic endpoint)
france_url = "https://10times.com/le-cuir-a-paris"

# Where chromedriver is located on my machine
# PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(env.PATH, options=chrome_options) 
driver.get(france_url) 
driver.maximize_window()
sleep(10)


titles = []
event_single = []


# Grabs all text elements in table, have to clean up data.
timings = driver.find_element_by_xpath('//*[@id="content"]/section[3]/table')

# Grabs all the details from table into a list that needs to be formatted before saving
text = [timings.get_attribute('innerText').replace('\n', ',')]
print("Table details: \n " , text)
print('<----------------------------------------------->')
print('<----------------------------------------------->')

# Gets the description
desc = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div/section[1]/p').text
print("Event Description: \n ", desc)
print('<----------------------------------------------->')


address = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[4]').text
print("Address: \n ", address)
   
driver.close()
driver.quit()









    
    