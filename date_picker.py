
from datetime import date,timedelta


# TODO Name these better
url_list = []
url_ranges = []
start_end_pair_list=[]
url_dates = []


# TODO automate start and end dates, based on current_date


start_dt = date(2020, 11, 5)
end_dt = date(2021, 11, 4)

def create_url():

    def dateRangeStart(start_date, end_date):
        for n in range(0, int((end_date - start_date).days) + 1, 7):
            yield start_date + timedelta(n)
            yield start_date + timedelta(n + 6)
    for dt in dateRangeStart(start_dt, end_dt):
        url_dates.append(dt.strftime("%Y-%m-%d"))
    
    # Grouping into start and end dates for 1 week range. 
    step = 2     
    for x in range(0, len(url_dates)-step+1, step):
        start_end_pair_list.append(url_dates[x:x+step])

    

    # Creating the url's with start and end dates added
    for url in url_list:
        for dates in start_end_pair_list:
            url_ranges.append(f'{url}?datefrom={dates[0]}&dateto={dates[1]}')
            
     

# Pulls base url from countries txt file 
with open('countries.txt') as countries:
    line = countries.readline()
    while line:
        line = countries.readline()
        url_list.append(line.strip().replace('\n', ''))
    create_url()
    

# writing new Urls to txt file 
with open('event_date_range.txt', 'w') as file:
        for url in url_ranges:
            # Had this in here to avoid pulling url's that do not contain valid url, happened once but I believe I fixed it, so may not need this check. 
            if not url.startswith('?'): 
                    file.write(url)
                    file.write('\n')
        
            
           
 




