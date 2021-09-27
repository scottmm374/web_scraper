from bs4.element import whitespace_re
from bs4 import BeautifulSoup
import requests

#    Testing different events to find consistent elements to grab # 
# URL = 'https://10times.com/plastics-recycling-world-exhibition'
URL = "https://10times.com/legion-sports-fest"
# URL = 'https://10times.com/med-tech-innovation'


response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup.prettify())



# Grabbing elements from header at top, Format, Event Name, and Event Location, and Date

# Narrow down elements only in header
top_wrapper = soup.find('section', attrs={'class' : 'page-wrapper'})

# Grabs Format type
format_type = top_wrapper.find('span', attrs={'class' : 'label label-success me-1 fs-12 rounded-2'})
# print(repr(format_type.string))


# Grabs the event name
title = top_wrapper.h1.get_text()
# for string in top_wrapper.h1.stripped_strings:
#     print()
# print(title)

# Grabs location from header

location_finder = top_wrapper.findAll('div', attrs={'class': 'mb-0 fs-20'})
# 2 divs with same class name, second one has text needed. 
location = location_finder[1].get_text()

# print(location)

# Grabbing description of event. This will need some conditionals, since some have a link to expand text 
description = soup.find('div', attrs={'id': 'content'})
# print(description.p.get_text())


# TABLE 

table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'})

# Table First Row section
table_row = table_details.find('tr', attrs={'id': 'hvrout1'})

# Timings, this will also need conditionals to search for more timings if expand is present
timings = table_row.find('h2').next_sibling.strip().replace('\n', '').replace(' ', '')


# Grabbing catagories 
table_data_cell = table_details.find('td', attrs={'id': 'hvrout2'})
for catagory in table_data_cell.findAll('a'):
    print(catagory.get_text())





# print((catagories))