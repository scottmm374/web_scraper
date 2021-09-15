from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import env
import random

from selenium.webdriver.chrome.options import Options

# chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
random_sleep = round(random.randint(4,200) /3, 4)
# sleeping = round((random_sleep / 7), 4)
print(random_sleep)

# URL france events (Will change to dynmaic endpoint)
france_url = "https://10times.com/le-cuir-a-paris"

# Where chromedriver is located on my machine
# PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(env.PATH, options=chrome_options)  
driver.get(france_url) 
driver.maximize_window()
sleep(random_sleep)
events_france = []
event_single = []
titles = []




# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
sleep(random_sleep)
while True:


    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    events = driver.find_element_by_xpath('//*[@id="listing-events"]')

    if events:
        sleep(random_sleep)
        event = events.find_element_by_tag_name('h2')
        event_single.append(event)
    else:
       print('cant find')
       driver.close()
       driver.quit()
    
    # event = [x for x in events.find_elements_by_tag_name("a")]
    # titles = [x.text for x in events.find_elements_by_tag_name("h2")]
    # print(titles)
    
    # Wait to load page
    sleep(random_sleep)


    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# driver.close()
originalWindow = driver.current_window_handle


driver.close()
driver.quit()




print(len(events_france))
print(events_france)




# try:
#     title = driver.find_element_by_css_selector('.col-md-10 > div:nth-child(3) > h1:nth-child(1)')
#     events_france.append(title)
#     print("Title", title)

# except:
#     print('Not found')
#     driver.quit()

# time.sleep(random_sleep)

# try:
#     date = driver.find_element_by_css_selector('div.mb-0:nth-child(4) > span:nth-child(2)')
#     events_france.append(date)
#     print("links")

# except:
#     print('Not found')
#     driver.quit()
# try:
#     links = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/h2/a')
#     print("links")
#     driver.execute_script("arguments[0].click();", links)

# except:
#     print('Not found')
#     driver.quit()
#     try:
#     links = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/h2/a')
#     print("links")
#     driver.execute_script("arguments[0].click();", links)

# except:
#     print('Not found')
#     driver.quit()
#     try:
#     links = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/h2/a')
#     print("links")
#     driver.execute_script("arguments[0].click();", links)

# except:
#     print('Not found')
#     driver.quit()
#     try:
#     links = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/h2/a')
#     print("links")
#     driver.execute_script("arguments[0].click();", links)

# except:
#     print('Not found')
#     driver.quit()
# try:
#     links = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/h2/a')
#     print("links")
#     driver.execute_script("arguments[0].click();", links)

# except:
#     print('Not found')
#     driver.quit()




# events = driver.find_element_by_xpath('//*[@id="listing-events"]')




driver.close()
driver.quit()








