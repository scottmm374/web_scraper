from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
# driver.close()


# grabbing all countries and storing in list
countries = []

country_scrap = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/section/table/tbody/tr[2]/td[1]/a').get_attribute('href')
countries.append(country_scrap)
print(countries)




