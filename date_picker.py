
from datetime import date
from dateutil.relativedelta import relativedelta

url_list = []
url_ranges = []


# Generates url with a one month date range appended to country event url. 
# TODO Adjust date ranges to smaller increments since ANY date range only allows a MAX of 400 events to be returned. 
def date_range_generator (num_s, num_e, url):
   
    start_date = date.today() + relativedelta(months=-num_s)
    one_month = date.today() + relativedelta(months=-num_e)
    url_ranges.append(f'{url}?datefrom={start_date}&dateto={one_month}')
    
    
# generates start and stop variables needed for date range generator function 
# TODO Need to adjust
def change_range():
    for x in range(len(url_list)-1):
        num_start = 13
        num_stop = 12
        while num_stop != 0:
            num_start = num_start - 1
            num_stop = num_stop - 1
            date_range_generator(num_start, num_stop, url_list[x])


# Pulls base url from countries txt file 
with open('countries.txt') as countries:
    line = countries.readline()
    while line:
        line = countries.readline()
        url_list.append(line.strip().replace('\n', ''))
    change_range()

# checking that original list matched correct length when adding one month date range (subtracting one because last url is empty str, will adjust later in original write function)
print(len(url_ranges), (len(url_list)-1) *12)

# writing new Urls to text file with one year previous to todays date incremented monthy 
with open('event_date_range.txt', 'w') as file:
        for url in url_ranges:
                file.write(url)
                file.write('\n')
        
            
           
        

