from bs4 import BeautifulSoup
from urllib.error import URLError
import requests
import csv
import random
import time
import re


def random_sleep():
    sleeping = round(random.randint(5,125) /7, 6)
    print('Random sleep should be', sleeping)
    return sleeping



collected_data = []

def grab_url():
    
    with open('event_url.txt') as f:
                line = f.readline()
                while line:
                    line = f.readline().strip().replace('\n', '')
                    print('<------------------------------->')
                    print(line)
                    time.sleep(random_sleep())
                    if not line:
                        print('no line')
                        break
                    get_details(line)
                


def get_details(url):
   
    URL = url
    event_single = {
        'Event_url': None,
        'Event_name': None,
        'Event_venue_name': None,
        'Venue_address' : None,
        'Format' : None, 
        'Dates' : None,
        'Location' : None,
        "Entry_fees" : None,
        'Estimated_turnout' : [],
        'Categories' : [],
        'Frequency' : None,
        'Organizer' : None,
        'Editions' : None,
        'Timings' : None,
    }
   
    '''
    In try catch to avoid stopping the scraper because of a missed element.
    A few Elements need conditionals, I will list on the Readme.
    '''

# Check if url valid
    try:
        response = requests.get(URL, allow_redirects=False)
        response.raise_for_status()
    except URLError as ue:
            print("The Server Could Not be Found")

#    Adding event URL to event_single to track url data retrieved from
    event_single['Event_url'] = URL
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())
    # print(soup.get_text())

    # FORMAT, EVENT NAME, DATES, LOCATION (pulled from Header)

    try: 
        top_wrapper = soup.find('section', attrs={'class' : 'page-wrapper'})
        
    except:
        print('Couldnt find top-wrapper')
    try:
        location_finder = top_wrapper.findAll('div', attrs={'class': 'mb-0 fs-20'})
        
    except:
        print('Couldnt find location_finder')

    # FORMAT TYPE
    try: 
        format_type = top_wrapper.find('span', attrs={'class' : 'label label-success me-1 fs-12 rounded-2'})
        event_single['Format'] = format_type.string
    except:
        print('Couldnt find format_type')

    # EVENT NAME
    try:
        event_name = top_wrapper.h1.get_text()
        event_single['Event_name'] = event_name
    except:
        print('Couldnt find event name')

    # Event DATES
   
    try:
        dates = location_finder[0].get_text().split('\\', 1)[0].replace('Add To Calendar', '').replace('New Date Reminder', "")
        event_single['Dates'] = dates
    except:
        print('Couldnt find Dates')

    # LOCATION
    try:
        location = location_finder[1].get_text()
        event_single['Location'] = location
    except:
        print('Couldnt find title')
   
    # DESCRIPTION (paragraph)
    try:
        description_section = soup.find('div', attrs={'id': 'content'})
    except:
        print('Couldnt find description_section')
    try:
        description = description_section.p.get_text()
        event_single['Description']= [description.strip()]
    except:
        print('Couldnt find Description')
   


    # TABLE THAT CONTAINS ENTRY FEES, TIMINGS, ESTIMATED TURNOUT, CATEGORIES, VENUE NAME, EDITIONS, ORGANIZER
    try:
        table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'}).find_all('tr')
    except:
        print('Couldnt find table_details')

    # Table section that contains ENTRY FEES, TIMINGS
    # try:
    #     table_row = table_details.find('tr', attrs={'id': 'hvrout1'})
    # except:
    #     print('Couldnt find table_row')

# Timings
# TODO:  some entry_fees have a link to check website, which is behind login, others have a table(or two)linked at the bottom of the page. Needs a few different conditionals to work properly 
    try:
        timings = table_details[0].next
        event_single["Timings"] = timings.get_text(',', strip=True).replace("Timings", "").replace("(expected)", "").replace(",Not Verified", "").replace("(General)", "")
    except:
        print('Couldnt find Timings')

     # Entry_fees
    try:
      entry_fees = timings.next_sibling
      event_single["Entry_fees"] = entry_fees.get_text(',', strip=True).replace("Entry Fees,", "").replace("\n", "")
       
    except:
        print('Couldnt find Timings')

    # ESTIMATED TURNOUT
    # TODO: This can have at least 3 different fields, visitor, exhibitor, delegates that I have found so far. Need to adjust this one for each senario
    try:
        estimated_turnout = table_details[1].next
        event_single["Estimated_turnout"] = estimated_turnout.get_text().replace("Estimated Turnout", "").replace("Estimated Count", "").replace("Based on previous editions", "")
      

        
    except:
            print('Couldnt find estimated turnout')

# CATEGORIES 
    try:
        
       categories = estimated_turnout.next_sibling
       event_single["Categories"] = categories.get_text().replace("Category & Type", "").replace("Conference", "").replace("Trade Show", "")
    except:
        print('Couldnt find table_row')


# VENUE NAME
    try:
   
        venue_list = []
        map_location = soup.find('section', attrs={'id': 'map_dirr'})
        for venue in map_location.findAll('a'):
            venue_list.append(venue.get_text())
        event_single['Event_venue_name'] = venue_list[1].strip().replace('\n', '')
    except:    
        print('Couldnt find venue_list')

# VENUE ADDRESS - FIXME: Wont be located for virtual events, so need conditional
    try:
        venue_address = map_location.find('p')
        addy = []
        for address in venue_address.find_all('span'):
            addy.append(address.get_text())
        event_single['Venue_address'] = addy
    except:
        print("Venue addy not found")

# EDITIONS AND FREQUENCY
    try:
        editions_frequency = table_details[2].next
        # table_section_3 = soup.find('tr', attrs={'id': 'hvrout3'})
        edition_freq = []
        for element in editions_frequency.stripped_strings:
                edition_freq.append(element.replace('Interested', ''))
        index_marker = edition_freq.index("Frequency")
        event_single['Editions'] = edition_freq[1:index_marker]
        event_single['Frequency'] = edition_freq[index_marker + 1]
        print(edition_freq)
    except:
        print("Editions or Frequency not found")

# ORGANIZATION
    try:
        organization = soup.find(id="org-name").text
        event_single['Organizer'] = organization
    except:
        print('Org not found')

    collected_data.append(event_single)

grab_url()

def create_csv(data):
    print("data", data)
    fieldnames = ["Event_url","Event_name", "Event_venue_name", "Venue_address", 'Format', 'Dates', 'Location', "Entry_fees", 'Estimated_turnout', 'Categories', 'Frequency', 'Organizer', 'Editions', 'Timings', 'Description']
    print("In writing to csv")

    # write to csv 
    with open('events.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames, delimiter="|")
        writer.writerow({x: x for x in fieldnames})

        for item in data:
            writer.writerow(item)

create_csv(collected_data)
   