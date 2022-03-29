
from datetime import date, datetime,timedelta


# TODO Name these better
url_list = []
url_ranges = []
start_end_pair_list=[]
url_dates = []


# TODO automate start and end dates, based on current_date (Currently set to one year previous. Adjust for Monthly once Initial data is pulled.
today = date.today()
one_year = date.today() - timedelta(days=365)


start_dt = date(one_year.year, one_year.month, one_year.day)
end_dt = date(today.year, today.month, today.day)

def create_url():

    def dateRangeStart(start_date, end_date):
        for n in range(0, int((end_date - start_date).days) + 1, 7):
            yield start_date + timedelta(n)
            yield start_date + timedelta(n + 6)
    for dt in dateRangeStart(start_dt, end_dt):
        url_dates.append(dt.strftime("%Y-%m-%d"))
    
    # Grouping into start and end dates for 1 week range. Larger countries will probably require a smaller date range to avoid logging in.
    step = 2     
    for x in range(0, len(url_dates)-step+1, step):
        start_end_pair_list.append(url_dates[x:x+step])

    # Creating the url's with start and end dates added
    for url in url_list:
        for dates in start_end_pair_list:
            url_ranges.append(f'{url}?datefrom={dates[0]}&dateto={dates[1]}')
            
   

# Pulls base url from countries txt file 
with open('countries.txt', 'r') as countries:
    line = countries.readline()
    while line:
        line = countries.readline()
        url_list.append(line.strip().replace('\n', ''))
    create_url()
    

# URL's with updated country and date range
with open('event_date_range.txt', 'w') as file:
        for url in url_ranges:
                file.write(url)
                file.write('\n')

         
           





