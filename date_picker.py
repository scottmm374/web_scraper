
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import csv


todays_date = date.today()

def date_range_generator (num_s, num_e):
    todays_date = date.today()
   
    start_date = date.today() + relativedelta(months=-num_s)
    one_month = date.today() + relativedelta(months=-num_e)
    url = (f'?datefrom={start_date}&dateto={one_month}')
    
    print(url)



# print(start_date)
# print(one_month)

# url = (f'?datefrom={start_date}&dateto={one_month}')
# print(url)
# print(one_month == todays_date)


def check_range():
    num_start = 13
    num_stop = 12
    while num_stop != 0:
        num_start = num_start - 1
        num_stop = num_stop - 1
        date_range_generator(num_start, num_stop)

check_range()

# with open('countries.txt') as countries:
#     line = countries.readline()
#     while line:
#         line = countries.readline()
#         while one_month != todays_date:
#             url = (f'{line}?datefrom={start_date}&dateto={one_month}')
#             num_start = num_start - 1
#             num_stop = num_stop - 1
        
# "https://10times.com/usa?datefrom=2021-09-01&dateto=2022-10-07"

