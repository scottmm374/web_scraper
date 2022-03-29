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
        'Country': None,
        "Date_range": None,
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
    
    '''

# Check if url valid
    try:
        response = requests.get(URL, allow_redirects=False)
        response.raise_for_status()
    except URLError:
            print("The Server Could Not be Found")

#    Adding event URL to track where data retrieved from
    event_single['Event_url'] = URL
    soup = BeautifulSoup(response.content, "html.parser")
    

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
        get_event_dates = location_finder[0]
        dates = get_event_dates.get_text().split('\\', 1)[0].replace('Add To Calendar', '').replace('New Date Reminder', "")
        event_single['Dates'] = dates
    except:
        print('Couldnt find Dates')

    # LOCATION
    try:
        location = location_finder[1].get_text()
        event_single['Location'] = location
    except:
        print('Couldnt find title')
   
    # DESCRIPTION
    try:
        description_section = soup.find('div', attrs={'id': 'content'})
    except:
        print('Couldnt find description_section')
    try:
        description = description_section.p.get_text(strip=True)
        event_single['Description']= description
    except:
        print('Couldnt find Description')
   


# TABLE THAT CONTAINS ENTRY FEES, TIMINGS, ESTIMATED TURNOUT, CATEGORIES, VENUE NAME, EDITIONS, ORGANIZER
    try:
        table_details = soup.find('table', attrs={'class': 'table noBorder mng w-100 trBorder'}).find_all('tr')
    except:
        print('Couldnt find table_details')


   

# Many entry_fees have an external link instead of available on website, which is behind login.
# Others have a table(or two)linked at the bottom of the page (View Details). 

    
# Timings
    try:
        get_timings = table_details[0].next
        clean_timings = get_timings.get_text().replace("Timings", "").replace("(expected)", "").replace("Not Verified", "").replace("(General)", "").replace('\n', " ")
        timings = " ".join(re.split("\s+", clean_timings, flags=re.UNICODE))
        event_single["Timings"] = timings
    except:
        print('Couldnt find Timings')

     # Entry_fees
    try:
        get_entry_fees = get_timings.next_sibling.get_text().replace("Entry Fees", " ").replace('\n', " ").replace('View Details', ' (View Details)')
    
        entry_fees = " ".join(re.split("\s+", get_entry_fees, flags=re.UNICODE))
      

        event_single["Entry_fees"] = entry_fees
       
    except:
        print('Couldnt find Entry Fees')

    # ESTIMATED TURNOUT
    # Estimated turnout has more then one type, visitor, exhibitor, and delegates.  
    try:
        get_estimated_turnout = table_details[1].next
        clean_estimated_turnout = get_estimated_turnout.get_text().replace("Estimated Turnout", " ").replace("Estimated Count", " ").replace("Based on previous editions", " ").replace('upto', 'up to').replace('\n', " ")
        estimated_turnout = " ".join(re.split("\s+", clean_estimated_turnout, flags=re.UNICODE))
        event_single["Estimated_turnout"] = estimated_turnout
      

        
    except:
            print('Couldnt find estimated turnout')

    # CATEGORIES 
    try:
        
       get_categories = get_estimated_turnout.next_sibling
       clean_categories = get_categories.get_text().replace("Category & Type", "").replace("Conference", "").replace("Trade Show", "")
       categories = " ".join(re.split("\s+", clean_categories, flags=re.UNICODE))

       event_single["Categories"] = categories
    except:
        print('Couldnt find table_row')


    # VENUE NAME
    try:
        # DO NOT TARGET anchor tags, Inconsistent, Grab event name from alt text in map image.
        get_map_location = soup.find(id='map_dirr').find('img', alt=True)
        venue_name = get_map_location['alt'].replace("map of ", '')
        event_single['Event_venue_name'] = venue_name
       
    except: 
        # If not found, its a virtual event.
        event_single['Event_venue_name'] = "Virtual"   
        print('Couldnt find venue_list')

    # VENUE ADDRESS 
    try:
         get_venue_address = soup.find(id="map_dirr").get_text(strip=True)
         venue_address = get_venue_address.replace('Venue Map & Directions', "").replace("Get Directions", "")
         event_single['Venue_address'] = venue_address
         
    except:
        # If not found, its a virtual event.
        event_single['Venue_address'] = 'Virtual'
        print("Venue addy not found")

    # EDITIONS AND FREQUENCY
    try:
        editions_frequency = table_details[2].next
        edition_freq = []

        for element in editions_frequency.stripped_strings:
                edition_freq.append(element.replace('Interested', ''))
        index_marker = edition_freq.index("Frequency")

        event_single['Editions'] = edition_freq[1:index_marker]
        event_single['Frequency'] = edition_freq[index_marker + 1]
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
    fieldnames = ["Country", "Date_range", "Event_url","Event_name", "Event_venue_name", "Venue_address", 'Format', 'Dates', 'Location', "Entry_fees", 'Estimated_turnout', 'Categories', 'Frequency', 'Organizer', 'Editions', 'Timings', 'Description']
    print("In writing to csv")

    # write to csv 
    with open('events.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames, delimiter="|")
        writer.writerow({x: x for x in fieldnames})

        for item in data:
            writer.writerow(item)

create_csv(collected_data)
   