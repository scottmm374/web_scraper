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
france_url = "https://10times.com/france"


def random_sleep():
    sleeping = round(random.randint(4,150) /3, 4)
    print('Random sleep should be', sleeping)
    return sleeping

def random_mouse_hover(drive):
    ActionChains(drive).move_by_offset(random.uniform(1, 20), random.uniform(1, 20)).perform()
    time.sleep(random_sleep())


    
driver.get(URL) 
driver.maximize_window()
random_mouse_hover(driver)
start = time.time()
time.sleep(random_sleep())
end = time.time()
print(f"first took {(end - start):.5f} seconds")



 
def login():
    try:
        login_link = driver.find_element_by_xpath('//*[@id="loginHide"]')
        print('found login')
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
        
        login_email = driver.find_element_by_xpath('//*[@id="valEmail"]')
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
        check_box = driver.find_element_by_xpath('//*[@id="i2"]')
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
        next_btn = driver.find_element_by_xpath('//*[@id="send"]')
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
        enter_pswd = driver.find_element_by_xpath('//*[@id="otp_box"]/input')
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
        pswd_next_btn = driver.find_element_by_xpath("//input[@value='Next']")
        print('found pswd next')
        driver.execute_script("arguments[0].click();", pswd_next_btn)

    except:
        print('pswd next not found')
        driver.quit()


    



""" Grabbing all countries and storing in list, will use to add endpoints to url to access different country specific events"""

def countries_grab(cb):
    countries = []
    random_mouse_hover(driver)
    try:
        btn = driver.find_element_by_xpath('//*[@id="country-btn"]')
        print("Country button found")
        driver.execute_script("arguments[0].click();", btn)
        print("Country button clicked")

    except:
        print("Country button NOT found")
        driver.quit()

    start = time.time()
    time.sleep(random_sleep())
    end = time.time()
    print(f"country button took {(end - start):.5f} seconds")
    

    try:
        drop_down = driver.find_element_by_xpath('//*[@id="country"]')
        print("dropdown found")
        options = [x for x in drop_down.find_elements_by_tag_name("option")]

    except:
        print("dropdown NOT found")
        driver.quit()
    print('SUCCESS')
    for element in options:
        countries.append(element.get_attribute("value"))

    with open('countries.txt', 'w') as file:
        try:
            for country in countries:
                file.write(f'https://10times.com{country}')
                file.write('\n')
        except:
            driver.close()
            driver.quit()  
    driver.close()
    driver.quit()

countries_grab(login())

# !TRYING France SCROLL 

# event_single = []

# driver.get(france_url)
# driver.maximize_window()
# sleep(random_sleep)


# #  !Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# sleep(random_sleep)

# # ! SCROLL through france events

# while True:
    
#     # !Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # events = driver.find_element_by_xpath('//*[@id="listing-events"]')

#     # !wait to load page
#     sleep(random_sleep)

 


#     # !Grabbing titles in France to append to end of base url
#     events = driver.find_element_by_xpath('//*[@id="listing-events"]')
#     sleep(random_sleep)
#     event = [x for x in events.find_elements_by_class_name("text-decoration-none")]
#     # event = events.find_element_by_tag_name('a')
#     # event_single.append(event)
    
#     titles = [x.text for x in events.find_elements_by_tag_name("h2")]
#     print(titles)
    
   

#     # !Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height



# originalWindow = driver.current_window_handle



 









    









