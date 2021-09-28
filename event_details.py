from bs4.element import whitespace_re
from bs4 import BeautifulSoup
import requests
import re

#    Testing different events to find consistent elements to grab # 
# URL = 'https://10times.com/plastics-recycling-world-exhibition'
# URL = "https://10times.com/legion-sports-fest"
# URL = 'https://10times.com/med-tech-innovation'
URL = 'https://10times.com/home-based-travel-agent-forum-exhibition'  
# URL = 'https://10times.com/pour-lamour-du'


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


# Grabs location from header

location_finder = top_wrapper.findAll('div', attrs={'class': 'mb-0 fs-20'})
# 2 divs with same class name, second one has text needed. 


location = location_finder[1].get_text()
event_single['Location'] = [location]


# Grabbing description of event. This will need some conditionals, since some have a link to expand text 
description_section = soup.find('div', attrs={'id': 'content'})
description = description_section.p.get_text()
event_single['Description']= [description]


# * TABLE 

table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'})

# Table First Row section
table_row = table_details.find('tr', attrs={'id': 'hvrout1'})
search_row = table_row.findAll('h2')
for x in search_row:
    if x.text == 'Entry Fees':
       event_single['Entry_fees'] = [x.next_sibling.strip().replace('\n', '')]
    
another_list = []
# for x in table_row.descendants:
    # fee = x.get_text().strip().replace('\n', '')
    # print(x)
    # another_list.append(fee)
# print(another_list[1])


# for fee in table_row.find('td', attrs={"class" :'dfdgg'}):
# print(search_row.get_text())

# for fee in table_row.findAll('td', attrs={'class': 'width:50%;' }):
#     print(fee)

"""
    Timings, this will also need conditionals to search for more timings if expand is present
    ? UPDATE changed to td and stripped strings, returns everything without need for clicking link (view more)

"""
time_list = []
for time in table_row.find('td').stripped_strings:
    timings = time.strip().replace('\n', '').replace(' ', '')
    time_list.append(timings)

if time_list[-1] == 'ViewMore':
    time_list.pop()
event_single['Timings'] = time_list[1:]



# print(time_list)

#  Entry fees

# entry_fee = fees.find('h2').stripped_strings
# for fee in table_row.find('td', attrs={'class': 'width:50%;' }).get_text():


# *  Estimated turnout 
#  * <----------------------------------------------->
turnout = table_row.next_sibling
my_list = []

for nums in (turnout.findAll('a')):
    
    my_list.append(nums.get_text().strip())

visitors = (f'{my_list[0]} Visitors')
exhibitors = (f'{my_list[1]} Exhibitors')
# print(my_list[:2])
# print(f'{my_list[0]} Visitors \n {my_list[1]} Exhibitors')
event_single['Estimated_turnout'] = [visitors, exhibitors]




# * CATAGORIES 
table_data_cell = table_details.find('td', attrs={'id': 'hvrout2'})
for catagory in table_data_cell.findAll('a'):
    event_single['Categories'] = [catagory.get_text()]


#  * Venue_name
venue_list = []
map_location = soup.find('section', attrs={'id': 'map_dirr'})
for venue in map_location.findAll('a'):
    venue_list.append(venue.get_text())
event_single['Event_venue_name'] = [venue_list[1].strip().replace('\n', '')]


venue_address = map_location.find('p')
addy = []
for address in venue_address.find_all('span'):
    addy.append(address.get_text())
event_single['Venue_address'] = addy


table_section_3 = soup.find('tr', attrs={'id': 'hvrout3'})
# TODO  Need to format the list to exclude headers
edition_freq = []
for element in table_section_3.find('td').stripped_strings:
    edition_freq.append(element)
# print(edition_freq)

'''
Originally searched for h3 with id, but different events place the venue name within other tags, so instead I searched for the ID
'''
organization = soup.find(id="org-name").text
event_single['Oragnizer'] = [organization]
print(event_single)