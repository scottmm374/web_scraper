
from selenium.webdriver.common.action_chains import ActionChains
import random
import time


def random_sleep():
    sleeping = round(random.randint(5,125) /7, 6)
    print('Random sleep should be', sleeping)
    return sleeping


    # Random Mouse function to similate the occasional Mouse movements.
def random_mouse_hover(drive):
    ActionChains(drive).move_by_offset(random.uniform(1, 15), random.uniform(1, 15)).perform()
    time.sleep(random_sleep())
