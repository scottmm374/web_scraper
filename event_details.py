from bs4.element import whitespace_re
from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as pd
import random
import time

#    Testing different events Manually using them works, with the exception on a few. Need to adjust those, all exhibitor issue

# URL = 'https://10times.com/home-based-travel-agent-forum-exhibition'  works
# URL = 'https://10times.com/pour-lamour-du'
# URL ='https://10times.com/summer-conference-on-womens-health'
# URL ='https://10times.com/epigenetics-conference-nassau'
# URL ='https://10times.com/insol-international-bahamas-seminar'
# ! URL ='https://10times.com/nahad-annual-meeting-convention-nassau'  exhibitors = (f'{my_list[1]} Exhibitors')  IndexError: list index out of range
#  !URL ='https://10times.com/clc-nassau'  exhibitors = (f'{my_list[1]} Exhibitors')IndexError: list index out of range
# URL ='https://10times.com/frontiers-in-photochemistry-conference' 
# ! URL ='https://10times.com/business-finance-summit' exhibitors = (f'{my_list[1]} Exhibitors')IndexError: list index out of range
# URL ='https://10times.com/internal-medicine-for-primary-care-cardio-gastro-i'
# URL ='https://10times.com/caribbean-insurance-conference'
# URL ='https://10times.com/internal-medicine-for-primary-care-nassau'
# URL ='https://10times.com/dna-repair-replication-structures-and-cancer'
# ! URL ='https://10times.com/itic-americas' exhibitors = (f'{my_list[1]} Exhibitors')IndexError: list index out of range
# ! URL ='https://10times.com/genome-engineering' (f'{my_list[1]} Exhibitors')IndexError: list index out of range






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
    'Organizer' : None,
    'Editions' : None,
    'Description' : None,
    'Timings' : None,
}

url_list = []
with open('event_url.txt') as f:
    # print(" with open before for loop")
    line = f.readline()
    while line:
        print("grabbing", line)
        line = f.readline().strip().replace('\n', '')
        # url_list.append(line.strip().replace('\n', ''))
# print(url_list)      


        print("feeding", line) 
        response = requests.get(line, allow_redirects=False)
        soup = BeautifulSoup(response.content, "html.parser")
        # print(soup.prettify())
        
        # FORMAT, EVENT NAME, DATES, LOCATION (pulled from Header)
        top_wrapper = soup.find('section', attrs={'class' : 'page-wrapper'})
        location_finder = top_wrapper.findAll('div', attrs={'class': 'mb-0 fs-20'})
        format_type = top_wrapper.find('span', attrs={'class' : 'label label-success me-1 fs-12 rounded-2'})
        print(format_type.string)
        event_single['Format'] = [format_type.string]

        title = top_wrapper.h1.get_text()
        event_single['Event_name'] = [title]
        print(title)
        dates = location_finder[0].get_text().replace('Add To Calendar', '')
        event_single['Dates'] = [dates]
        location = location_finder[1].get_text()
        event_single['Location'] = [location]
        # <----------------------------------------------------------->
        # DESCRIPTION (paragraph)
        description_section = soup.find('div', attrs={'id': 'content'})
        description = description_section.p.get_text()
        event_single['Description']= [description]

        # <-------------------------------------------------------------->

        # TABLE THAT CONTAINS ENTRY FEES, TIMINGS, ESTIMATED TURNOUT, CATEGORIES, VENUE NAME, EDITIONS, ORGANIZER
        table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'})
        # Table section that contains ENTRY FEES, TIMINGS
        table_row = table_details.find('tr', attrs={'id': 'hvrout1'})
    #  TODO can cause error, occasionally not found
        # Entry Fees
        # search_row = table_row.findAll('h2')
        # for x in search_row:
        #     if x.text == 'Entry Fees':
        #         event_single['Entry_fees'] = [x.next_sibling.strip().replace('\n', '')]
        # Timings
        time_list = []
        for time in table_row.find('td').stripped_strings:
            timings = time.strip().replace('\n', '').replace(' ', '')
            time_list.append(timings)

        if time_list[-1] == 'ViewMore':
            time_list.pop()
        event_single['Timings'] = time_list[1:]

        #  TODO can cause error, occasionally not found
        # Estimated Turnout
        # turnout = table_row.next_sibling

        # my_list = []
        # for nums in (turnout.findAll('a')):
            
        #     my_list.append(nums.get_text().strip())

        # visitors = (f'{my_list[0]} Visitors')
        # exhibitors = (f'{my_list[1]} Exhibitors')

        # event_single['Estimated_turnout'] = [visitors, exhibitors]


        # CATAGORIES 
        table_data_cell = table_details.find('td', attrs={'id': 'hvrout2'})
        for catagory in table_data_cell.findAll('a'):
            event_single['Categories'] = [catagory.get_text()]

        #  Venue_name
        venue_list = []
        map_location = soup.find('section', attrs={'id': 'map_dirr'})
        for venue in map_location.findAll('a'):
            venue_list.append(venue.get_text())
        event_single['Event_venue_name'] = [venue_list[1].strip().replace('\n', '')]
        #  Venue Address
        venue_address = map_location.find('p')
        addy = []
        for address in venue_address.find_all('span'):
            addy.append(address.get_text())
        event_single['Venue_address'] = addy
        #  Editions and Frequency
        table_section_3 = soup.find('tr', attrs={'id': 'hvrout3'})

        edition_freq = []
        for element in table_section_3.find('td').stripped_strings:

                edition_freq.append(element)

        event_single['Editions'] = [edition_freq[1]]
        event_single['Frequency'] = [edition_freq[-1]]
        # print(edition_freq)


        # Organization
        organization = soup.find(id="org-name").text
        event_single['Organizer'] = [organization]

        

        '''
        Have to redo writing to csv, find a way to write headers with first pass and then append after to avoid overwrite, probably simple solution
        '''
        
        fieldnames = []

        for key, value in event_single.items():
                fieldnames.append(key)

    # initial write to csv 
        # with open('events.csv', 'w') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerow(event_single)

        #  Appending

        with open('events.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(event_single)

        
        
    
        
            
       



# Checking to see if formatted right in csv. 
df = pd.read_csv('events.csv')
print(df)


    # count = 0
#     print(count)

#     if count == 0:
#         fieldnames = []
#         for key, value in events.items():
#             fieldnames.append(key)
    
# # initial write to csv 
#         with open('events.csv', 'w') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerow(events)
    
#     if count > 0:
#     #  Appending to csv to avoid overwrite
#         with open('events.csv', 'a') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writerow(events)
#     count = count + 1
#     print(count)
# get_url()
# get_event_details(URL)
