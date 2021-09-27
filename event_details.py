from bs4.element import whitespace_re
from bs4 import BeautifulSoup
import requests

#    Testing different events to find consistent elements to grab # 
# URL = 'https://10times.com/plastics-recycling-world-exhibition'
# URL = "https://10times.com/legion-sports-fest"
URL = 'https://10times.com/med-tech-innovation'


response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup.prettify())



# Grabbing elements from header at top, Format, Event Name, and Event Location, and Date

# Narrow down elements only in header
top_wrapper = soup.find('section', attrs={'class' : 'page-wrapper'})

# Grabs Format type
format_type = top_wrapper.find('span', attrs={'class' : 'label label-success me-1 fs-12 rounded-2'})
print(repr(format_type.string))


# Grabs the event name
for string in top_wrapper.h1.stripped_strings:
    print(repr(string))
