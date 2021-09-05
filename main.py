from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import env

# chrome options
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-notifications')

# URL france events
url = "https://10times.com"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH, options=chrome_options) 


driver.get(url) 

# Issues with Exceptions thrown on button click (known issue with Chrome driver), so used this code to reach and activate button. 
driver.maximize_window()
time.sleep(5)


# Login
login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')

if(login_link):
    print('found login')
    driver.execute_script("arguments[0].click();", login_link)
else:
    print('Cant find Login')
    driver.quit()

time.sleep(5)

login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
time.sleep(5)
if(login_email):
    print('found email')
    login_email.send_keys(env.EMAIL)
else:
    print('Cant find email')
    driver.quit()
time.sleep(2)

# agreement button
check_box = driver.find_element_by_xpath('//*[@id="i2"]')
if(check_box):
    print('checkbox')
    driver.execute_script("arguments[0].click();", check_box)
else:
    print('Cant find checkbox')
    driver.quit()
time.sleep(2)


next_btn = driver.find_element_by_xpath('//*[@id="send"]')
if(next_btn):
    print('next')
    driver.execute_script("arguments[0].click();", next_btn)

else:
    print('Cant find next')
    driver.quit()
time.sleep(4)

enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
if(enter_pswd):
    print('found pswd')
    enter_pswd.send_keys(env.PSWD)
else:
    print('pswd not found')
    driver.quit()

time.sleep(2)

pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
if(pswd_next_btn):
    print('found pswd next')
    driver.execute_script("arguments[0].click();", pswd_next_btn)
   
else:
    print('pswd next not found')
    driver.quit()
# driver.quit()

print('We reached the end')



# btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
# driver.execute_script("arguments[0].click();", btn)


# # grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events
# countries = []

# time.sleep(7)
# drop_down = driver.find_element_by_xpath('//*[@id="country"]')

# options = [x for x in drop_down.find_elements_by_tag_name("option")]

# for element in options:
#     countries.append(element.get_attribute("value"))

# driver.close()




# print(countries)


#  Error after login and entering email.. checkbox
# Traceback (most recent call last):
#   File "/Users/michellescott/Documents/github/iearn/tentimes-scraper/main.py", line 31, in <module>
#     check_box = driver.find_element_by_xpath('//*[@id="i2"]').click()
#   File "/Users/michellescott/.local/share/virtualenvs/webscrape-vQ_GJror/lib/python3.9/site-packages/selenium/webdriver/remote/webelement.py", line 80, in click
#     self._execute(Command.CLICK_ELEMENT)
#   File "/Users/michellescott/.local/share/virtualenvs/webscrape-vQ_GJror/lib/python3.9/site-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
#     return self._parent.execute(command, params)
#   File "/Users/michellescott/.local/share/virtualenvs/webscrape-vQ_GJror/lib/python3.9/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
#     self.error_handler.check_response(response)
#   File "/Users/michellescott/.local/share/virtualenvs/webscrape-vQ_GJror/lib/python3.9/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
#   (Session info: chrome=92.0.4515.159)
