from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# URL france events
url = "https://10times.com"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH) 
driver.get(url) 

# Issues with Chrome locating button, so used this code to reach and activate button. 
driver.maximize_window()
btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
driver.execute_script("arguments[0].click();", btn)




