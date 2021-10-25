
from datetime import date, datetime, timedelta


# TODO Name these better
url_list = []
url_ranges = []
another_list=[]
url_dates = []


# TODO automate start and end dates
start_dt = date(2020, 10, 26)
end_dt = date(2021, 10, 26)

def create_url():

    def dateRangeStart(start_date, end_date):
        for n in range(0, int((end_date - start_date).days) + 1, 7):
            yield start_date + timedelta(n)
            yield start_date + timedelta(n + 6)
    for dt in dateRangeStart(start_dt, end_dt):
        url_dates.append(dt.strftime("%Y-%m-%d"))
        print(dt)
    
    # Grouping into start and end dates for 1 week range. 
    step = 2     
    for x in range(0, len(url_dates)-step+1, step):
        another_list.append(url_dates[x:x+step])

    global size
    size = (len(another_list))

    
    for url in url_list:
        for dates in another_list:
            url_ranges.append(f'{url}?datefrom={dates[0]}&dateto={dates[1]}')
            
     

# Pulls base url from countries txt file 
with open('countries.txt') as countries:
    line = countries.readline()
    while line:
        line = countries.readline()
        url_list.append(line.strip().replace('\n', ''))
    create_url()
    

# writing new Urls to text file with one year previous to todays date incremented Weekly
with open('event_date_range.txt', 'w') as file:
        for url in url_ranges:
            if not url.startswith('?'): 
                    file.write(url)
                    file.write('\n')
        
            
           
 




