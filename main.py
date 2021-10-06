from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import env
import random


chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(env.PATH, options=chrome_options)

URL = "https://10times.com"

'''
Adjusted some of these manually while testing how many events I can get with different date ranges. Date_picker needs to be adjusted to smaller ranges, may add date_picker as function here before each scroll rather then creating and saving urls to text file. 
'''
# France = 'https://10times.com/france?datefrom=2020-10-06&dateto=2020-11-05'
# France ='https://10times.com/france?datefrom=2020-11-06&dateto=2020-12-05'
# France ='https://10times.com/france?datefrom=2020-12-06&dateto=2021-01-05'
# France ='https://10times.com/france?datefrom=2021-01-06&dateto=2021-02-05'
# France ='https://10times.com/france?datefrom=2021-02-06&dateto=2021-03-05'
# France ='https://10times.com/france?datefrom=2021-03-06&dateto=2021-04-05'
# France ='https://10times.com/france?datefrom=2021-04-06&dateto=2021-05-05'
# France ='https://10times.com/france?datefrom=2021-05-06&dateto=2021-06-05'
# France ='https://10times.com/france?datefrom=2021-06-06&dateto=2021-07-05'
# France ='https://10times.com/france?datefrom=2021-07-06&dateto=2021-08-05'
# France ='https://10times.com/france?datefrom=2021-08-06&dateto=2021-09-05'
# France ='https://10times.com/france?datefrom=2021-09-06&dateto=2021-9-14'
# France ='https://10times.com/france?datefrom=2021-09-15&dateto=2021-09-22'
# France ='https://10times.com/france?datefrom=2021-09-23&dateto=2021-09-29'
France ='https://10times.com/france?datefrom=2021-09-30&dateto=2021-10-06'



# Random sleep function created to avoid hardcoded sleep being detected. Had issues with using hardcoded sleeps and being kicked out of the website. 
def random_sleep():
    sleeping = round(random.randint(4,100) /7, 4)
    print('Random sleep should be', sleeping)
    return sleeping


# Random Mouse function to similate the occasional Mouse movements generally expected when a person visits a webpage
def random_mouse_hover(drive):
    ActionChains(drive).move_by_offset(random.uniform(1, 20), random.uniform(1, 20)).perform()
    time.sleep(random_sleep())

'''
Login function, on landing page, needed for scroll function to continue on Events pages. Login popup after 5 scrolls while collecting events, so Login at start. 
MAY Not need this if we can adjust DATE ranges for Events effectivly. Larger countries like USA may have to use this function so Im keeping it here for now.  
'''

 
# def login():

    # driver.get(URL) 
    # driver.maximize_window()
    # random_mouse_hover(driver)

    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"first took {(end - start):.5f} seconds")

    # try:
    #     login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')
    #     print('found login')
    #     driver.execute_script("arguments[0].click();", login_link)
        
    # except:
    #     print('Cant find Login')
    #     driver.close()
    #     driver.quit()
    
    # random_mouse_hover(driver)

    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"Login took {(end - start):.5f} seconds")
    
    # try:
        
    #     login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
    #     print('found email')
    #     login_email.send_keys(env.EMAIL)
        
    # except:
    #     print('Cant find email')
    #     driver.quit()

   
    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"email took {(end - start):.5f} seconds")

    # try:
    #     check_box = driver.find_element_by_xpath('//*[@id="i2"]')
    #     print('checkbox')
    #     driver.execute_script("arguments[0].click();", check_box)
    # except:
    #     print('Cant find checkbox')
    #     driver.quit()

    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"check took {(end - start):.5f} seconds")

    # random_mouse_hover(driver)
    

    # try:
    #     next_btn = driver.find_element_by_xpath('//*[@id="send"]')
    #     print('next')
    #     driver.execute_script("arguments[0].click();", next_btn)

    # except:
    #     print('Cant find next')
    #     driver.quit()

    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"next took {(end - start):.5f} seconds")

    
    # try:
    #     enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
    #     print('found pswd')
    #     enter_pswd.send_keys(env.PSWD)
    # except:
    #     print('pswd not found')
    #     driver.quit()

    # start = time.time()
    # time.sleep(random_sleep())
    # end = time.time()
    # print(f"password took {(end - start):.5f} seconds")
    # random_mouse_hover(driver)
    
    # try:
    #     pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
    #     print('found pswd next')
    #     driver.execute_script("arguments[0].click();", pswd_next_btn)

    # except:
    #     print('pswd next not found')
    #     driver.quit()


    



""" Grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events"""

# def countries_grab(cb):
#     countries = []
#     random_mouse_hover(driver)
#     try:
#         btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
#         print("Country button found")
#         driver.execute_script("arguments[0].click();", btn)
#         print("Country button clicked")

#     except:
#         print("Country button NOT found")
#         driver.quit()

#     start = time.time()
#     time.sleep(random_sleep())
#     end = time.time()
#     print(f"country button took {(end - start):.5f} seconds")
    

#     try:
#         drop_down = driver.find_element_by_xpath('//*[@id="country"]')
#         print("dropdown found")
#         options = [x for x in drop_down.find_elements_by_tag_name("option")]

#     except:
#         print("dropdown NOT found")
#         driver.quit()
#     print('SUCCESS')

#     for element in options:
#         countries.append(element.get_attribute("value"))

#     with open('countries.txt', 'w') as file:
#         try:
#             for country in countries:
#                 file.write(f'https://10times.com{country}')
#                 file.write('\n')
#         except:
#             driver.close()
#             driver.quit()  
#     driver.close()
#     driver.quit()


# Scroll function to scroll event pages
def scroll_page():

    
    print("In the Scroll function")

    driver.get(France)
    driver.maximize_window()
    random_mouse_hover(driver)

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"Scroll took {(end - start):.5f} seconds")

    #  Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")


    random_mouse_hover(driver)

    while True:
        print("in while loop")

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        start = time.time()
        time.sleep(random_sleep())
        end = time.time()
        print(f"sleep for scroll took {(end - start):.5f} seconds")

         # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        print("headed to events function")
        get_event_urls_by_country()

        random_mouse_hover(driver)
    
    driver.delete_all_cookies()
    driver.close()
    driver.quit()
   
"""
Grabs event URLs AND event IDs. Added to a set to avoid duplicates with each scroll. 
"""
def get_event_urls_by_country():
    print('In events function')
    url_set = set() 
    check_id = set()
    events = driver.find_element_by_id("listing-events")
    titles = [x for x in events.find_elements_by_tag_name("h2")]

    for element in titles:
        check_id.add(element.get_attribute('id'))

    for event in titles:
        url_set.add(event.find_element_by_tag_name("a").get_attribute('href'))

    print(url_set)
    print(check_id)






    
# countries_grab(login())
scroll_page()





 









    









