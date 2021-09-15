from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import env
import random


# ! chrome options
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

URL = "https://10times.com"
france_url = "https://10times.com/france"

# Where chromedriver is located on my machine
# PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(env.PATH, options=chrome_options) 
random_sleep = round(random.randint(4,100) /3, 4)
print(random_sleep)
country_url = []
countries = []

driver.get(URL) 

driver.maximize_window()
sleep(random_sleep)

# ! Login
try:
    login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')

    print('found login')
    driver.execute_script("arguments[0].click();", login_link)
except:
    print('Cant find Login')
    driver.close()
    driver.quit()

sleep(random_sleep)


try:
    login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
    print('found email')
    login_email.send_keys(env.EMAIL)
except:
    print('Cant find email')
    driver.quit()
sleep(random_sleep)

# ! agreement button

try:
    check_box = driver.find_element_by_xpath('//*[@id="i2"]')
    print('checkbox')
    driver.execute_script("arguments[0].click();", check_box)
except:
    print('Cant find checkbox')
    driver.quit()
sleep(random_sleep)

# ! Next button 

try:
    next_btn = driver.find_element_by_xpath('//*[@id="send"]')
    print('next')
    driver.execute_script("arguments[0].click();", next_btn)

except:
    print('Cant find next')
    driver.quit()
sleep(random_sleep)

# ! Password entry


try:
    enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
    print('found pswd')
    enter_pswd.send_keys(env.PSWD)
except:
    print('pswd not found')
    driver.quit()

sleep(random_sleep)

#  !Password Submit button
try:
    pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
    print('found pswd next')
    driver.execute_script("arguments[0].click();", pswd_next_btn)

except:
    print('pswd next not found')
    driver.quit()


sleep(random_sleep)

# !TRYING France SCROLL 

event_single = []

driver.get(france_url)
driver.maximize_window()
sleep(random_sleep)


#  !Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
sleep(random_sleep)

# ! SCROLL through france events

while True:
    
    # !Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # events = driver.find_element_by_xpath('//*[@id="listing-events"]')

    # !wait to load page
    sleep(random_sleep)

 


    # !Grabbing titles in France to append to end of base url
    events = driver.find_element_by_xpath('//*[@id="listing-events"]')
    sleep(random_sleep)
    event = [x for x in events.find_elements_by_class_name("text-decoration-none")]
    # event = events.find_element_by_tag_name('a')
    # event_single.append(event)
    
    titles = [x.text for x in events.find_elements_by_tag_name("h2")]
    print(titles)
    
   

    # !Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



# originalWindow = driver.current_window_handle


# print(event_single)
# def scrape(link):
#     """
#     scrape function that takes in a link grabbed from the title
#     then clicks on the page
#     after sent the the page its then scrapped for all the information we need
#     """
#     driver.get(link)
#     time.sleep(sleep)
#     print(sleep)
#     title = driver.find_element_by_tag_name("h1").text
#     print(title)


# for eve in event:
#     if eve.text in titles:
#         events_france.append(eve.get_attribute("href"))
# total = 0
# for links in events_france:
#     scrape(links)
#     driver.switch_to.window(originalWindow)
#     total += 1

print(event_single)
print(titles)
driver.close()
driver.quit()


# Grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events


# try:
#     btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
#     driver.execute_script("arguments[0].click();", btn)

# except:
#     driver.quit()

# try:

#     drop_down = driver.find_element_by_xpath('//*[@id="country"]')
#     options = [x for x in drop_down.find_elements_by_tag_name("option")]

# except:
#     driver.quit()

# for element in options:
#     countries.append(element.get_attribute("value"))

# with open('countries.txt', 'w') as file:
#     try:
#         for country in countries:
#             file.write(f'https://10times.com{country}')
#             file.write('\n')
#     except:
#         driver.close()
#         driver.quit()  


 

# print(countries)
# driver.close()
# driver.quit() 








    









