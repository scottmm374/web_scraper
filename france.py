from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

from selenium.webdriver.chrome.options import Options

# chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
random_sleep = random.randint(4,300)
sleeping = round((random_sleep / 7), 4)
print(sleeping)
# URL france events

# URL france events (Will change to dynmaic endpoint)
france_url = "https://10times.com/le-cuir-a-paris"

# Where chromedriver is located on my machine
PATH = '../../drivers/chromedriver'

driver = webdriver.Chrome(PATH) 
driver.get(france_url) 
driver.maximize_window()
sleep(sleeping)
events_france = []
event_single = []
titles = []
# SCROLL_PAUSE_TIME = 20

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
sleep(sleeping)
while True:

    random_sleep = random.randint(4,300)
    sleep = round((random_sleep / 3), 4)

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    events = driver.find_element_by_xpath('//*[@id="listing-events"]')

    if events:
        sleep(sleeping)
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
    sleep(sleeping)


    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# driver.close()
originalWindow = driver.current_window_handle

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


# print(total)
driver.close()
driver.quit()




print(len(events_france))
print(events_france)


# Scroll works but not completly as of yet, needs some human timing and interactions. .
# ScrollNumber = 50
# for i in range(1, ScrollNumber):
#     time.sleep(random_sleep)
#     driver.execute_script('window.scrollTo(1,50000)')
#     time.sleep(random_sleep)

# grabbing all event href and storing in list to iterate through, each page
# events_france = []
# time.sleep(random_sleep)


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
# event = [x for x in events.find_elements_by_tag_name("a")]

# for eve in event:
#     events_france.append(eve.get_attribute("href"))


# print(len(events_france))
# print(events_france)
driver.close()
driver.quit()








