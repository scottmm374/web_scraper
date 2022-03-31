from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from helpers import random_mouse_hover
import time
import env
import random
import re
from helpers import random_sleep



chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
s = Service(env.PATH)
driver = webdriver.Chrome(service=s, options=chrome_options)

# Random sleep function created to avoid hardcoded sleep being detected. 

# def random_sleep():
#     sleeping = round(random.randint(4,125) /7, 6)
#     print('Random sleep should be', sleeping)
#     return sleeping


# Random Mouse function to similate the occasional Mouse movements.
# def random_mouse_hover(drive):
#     ActionChains(drive).move_by_offset(random.uniform(1, 15), random.uniform(1, 15)).perform()
#     time.sleep(random_sleep())


# Scroll function to scroll event pages, pages with several listings have lazy load(after 40 listings, scroll is used to trigger new load) 
def scroll_page(url):

    time.sleep(random_sleep())
    driver.get(url)
    driver.maximize_window()
    # random_mouse_hover(driver)

    time.sleep(random_sleep())
  
    #  Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")


    # random_mouse_hover(driver)

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random_sleep())
       

         # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        # random_mouse_hover(driver)
        get_event_urls_by_country()

        # random_mouse_hover(driver)
    
    # driver.delete_all_cookies()
    # driver.close()
    # driver.quit()


# def get_date_range_url():
#     with open('txt_csv/event_date_range.txt') as f:
#         for url in f:
#             if url.find('france') != -1:
            
#                 scroll_page(str(url))

"""
Grabs event URLs AND event IDs. Added to a set to avoid duplicates with each scroll. 
"""

def get_event_urls_by_country():
    
    url_set = set() 
    check_id = set()
   
    time.sleep(random_sleep())
    # driver.get(url)
    # driver.maximize_window()
    time.sleep(10)


    # ADDED because if no events during date range, site fills with with random previous events. 
    # no_upcoming = driver.find_element(By.xpath('//*[@id="12"]') I orig)inally targeted this way, but found some pages do not have this element at all. 
    # check_upcoming = no_upcoming.text
    src = driver.page_source
    text_found = re.search(r'No upcoming events', src)
    
    
    time.sleep(5)
    if not text_found:
   
        events = driver.find_element(By.id("listing-events"))
        titles = [x for x in events.find_elements(By.tagName("h2"))]

        for element in titles:
            check_id.add(element.get_attribute('id'))

        for event in titles:
            url_set.add(event.find_element(By.tagName("a").get_attribute('href'))
        
        
        with open('txt_csv/event_url.txt', 'w') as file:
            
            for url in url_set:
                file.write(url)
                file.write('\n')

       
    

# get_date_range_url()


# LOGIN AND GRAB COUNTRIES FUNCTIONS BELOW IF NEEDED

'''
Login function, on landing page, needed for scroll function to continue on Events pages. Login popup after 5 scrolls while collecting events, so Login at start. 
MAY Not need this if we can adjust DATE ranges for Events effectivly. Larger countries like USA may have to use this function so Im keeping it here for now.  
'''

#  If Login needed

def login(url):

    driver.get(url) 
    driver.maximize_window()
    random_mouse_hover(driver)

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"first took {(end - start):.5f} seconds")

    try:
        login_link = driver.find_element(By.xpath('//*[@id="loginHide"]'))
        driver.execute_script("arguments[0].click();", login_link)
        
    except:
        print('Cant find Login')
        driver.close()
        driver.quit()
    
    random_mouse_hover(driver)

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"Login took {(end - start):.5f} seconds")
    
    try:
        
        login_email = driver.find_element(By.xpath('//*[@id="valEmail"]'))        
        print('found email')
        login_email.send_keys(env.EMAIL)
        
    except:
        print('Cant find email')
        driver.quit()

   
    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"email took {(end - start):.5f} seconds")

    try:
        check_box = driver.find_element(By.xpath('//*[@id="i2"]'))  
        print('checkbox')
        driver.execute_script("arguments[0].click();", check_box)
    except:
        print('Cant find checkbox')
        driver.quit()

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"check took {(end - start):.5f} seconds")

    random_mouse_hover(driver)
    

    try:
        next_btn = driver.find_element(By.xpath('//*[@id="send"]'))    
        print('next')
        driver.execute_script("arguments[0].click();", next_btn)

    except:
        print('Cant find next')
        driver.quit()

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"next took {(end - start):.5f} seconds")

    
    try:
        enter_pswd = driver.find_element(By.xpath('//*[@id="otp_box"]/inp)ut')
        print('found pswd')
        enter_pswd.send_keys(env.PSWD)
    except:
        print('pswd not found')
        driver.quit()

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"password took {(end - start):.5f} seconds")
    random_mouse_hover(driver)
    
    try:
        pswd_next_btn = driver.find_element(By.xpath("//input[@value='Next'])")
        print('found pswd next')
        driver.execute_script("arguments[0].click();", pswd_next_btn)

    except:
        print('pswd next not found')
        driver.quit()


    


# """ Grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events"""


def countries_grab():
    driver.get(env.BASE_URL)
    countries = []

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"page load {(end - start):.5f} seconds")

    random_mouse_hover(driver)
    
    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"page load {(end - start):.5f} seconds")


    try:
        btn = driver.find_element(By.xpath('//*[@id="country-btn"])'))
        print("Country button found")
        driver.execute_script("arguments[0].click();", btn)
        print("Country button clicked")

    except:
        print("Country button NOT found")
        driver.quit()


    try:
        table = driver.find_element(By.id('content'))
        country_list = [x for x in table.find_elements(By.tagName('tr'))]
       
        
    except:
        print("dropdown NOT found")
        driver.quit()


    for element in country_list:
        # There are advertisements  mixed in returning none, this is to avoid those links
        if element.get_attribute('data-link') != None:
            countries.append(element.get_attribute("data-link"))
 
 

    with open('txt_csv/countries.txt', 'w') as file:
        try:
            for country in countries:
                file.write(f'{env.BASE_URL}{country}')
                file.write('\n')
        except:
            driver.close()
            driver.quit() 

    driver.close()
    driver.quit()



   



    
countries_grab()
# scroll_page()









 









    









