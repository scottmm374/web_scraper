
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import csv


todays_date = date.today()


url_list = []
url_ranges = []



def date_range_generator (num_s, num_e, url):
    # url = url_list[0]
   
    start_date = date.today() + relativedelta(months=-num_s)
    one_month = date.today() + relativedelta(months=-num_e)
    url_ranges.append(f'{url}?datefrom={start_date}&dateto={one_month}')
    
    
    
def change_range():
    for x in range(len(url_list)):
        # if x != url_list[-1]:
        num_start = 13
        num_stop = 12
        while num_stop != 0:
            num_start = num_start - 1
            num_stop = num_stop - 1
            date_range_generator(num_start, num_stop, url_list[x])


with open('countries.txt') as countries:
    line = countries.readline()
    while line:
        line = countries.readline()
        url_list.append(line.strip().replace('\n', ''))
    change_range()


print(len(url_ranges), len(url_list)*12)

        
            
           
        
# "https://10times.com/usa?datefrom=2021-09-01&dateto=2022-10-07"

