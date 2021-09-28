from bs4.element import whitespace_re
from bs4 import BeautifulSoup
import requests

#    Testing different events to find consistent elements to grab # 
# URL = 'https://10times.com/plastics-recycling-world-exhibition'
# URL = "https://10times.com/legion-sports-fest"
# URL = 'https://10times.com/med-tech-innovation'
URL = 'https://10times.com/home-based-travel-agent-forum-exhibition'


response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup.prettify())

event_single = {
    'Event_name': None,
    'Event_venue_name': None,
    'Venue_address' : None,
    'Format' : None, 
    'Dates' : None,
    'Location' : None,
    "Entry_fees" : None,
    'Estimated_turnout' : None,
    'Categories' : None,
    'Frequency' : None,
    'Oragnizer' : None,
    'Editions' : None,
    'Description' : None,
    'Timings' : None,
}


# Grabbing elements from header at top, Format, Event Name, and Event Location, and Date

# Narrow down elements only in header
top_wrapper = soup.find('section', attrs={'class' : 'page-wrapper'})

# Grabs Format type
format_type = top_wrapper.find('span', attrs={'class' : 'label label-success me-1 fs-12 rounded-2'})
event_single['Format'] = [repr(format_type.string)]
# print(repr(format_type.string))


# Grabs the event name
title = top_wrapper.h1.get_text()
event_single['Event_name'] = [title]
# for string in top_wrapper.h1.stripped_strings:
#     print()
# print(title)

# Grabs location from header

location_finder = top_wrapper.findAll('div', attrs={'class': 'mb-0 fs-20'})
# 2 divs with same class name, second one has text needed. 
location = location_finder[1].get_text()
event_single['Location'] = [location]

# print(location)

# Grabbing description of event. This will need some conditionals, since some have a link to expand text 
description_section = soup.find('div', attrs={'id': 'content'})
description = description_section.p.get_text()
event_single['Description']= [description]
# print(description.p.get_text())


# TABLE 

table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'})

# Table First Row section
table_row = table_details.find('tr', attrs={'id': 'hvrout1'})

# Timings, this will also need conditionals to search for more timings if expand is present
timings = table_row.find('h2').next_sibling.strip().replace('\n', '').replace(' ', '')
event_single['Timings'] = [timings]

# TODO Where I left off Estimated turnout
turn_list = []
turnout = table_row.next_sibling
# visitors = turnout.findAll('a').get_text()
my_list = []

for nums in (turnout.findAll('a')):
    
    # visitors = nums[0]
    # exhibitors = nums[1]
    my_list.append(nums.get_text().strip())

visitors = (f'{my_list[0]} Visitors')
exhibitors = (f'{my_list[1]} Exhibitors')
# print(my_list[:2])
# print(f'{my_list[0]} Visitors \n {my_list[1]} Exhibitors')
event_single['Estimated_turnout'] = [visitors, exhibitors]

# exibitors = turnout.find



# Grabbing catagories 
table_data_cell = table_details.find('td', attrs={'id': 'hvrout2'})
for catagory in table_data_cell.findAll('a'):
    event_single['Categories'] = [catagory.get_text()]
    # print(catagory.get_text())

    print(event_single)