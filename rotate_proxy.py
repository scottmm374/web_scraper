from bs4 import BeautifulSoup
import random
import requests



# proxies = [] # Will contain proxies [ip, port]



# Main function
def main():

    proxies = [] # Will contain proxies [ip, port]

# Getting proxies 
    proxies_req = requests.get('https://www.sslproxies.org/')

    soup = BeautifulSoup(proxies_req.content, 'html.parser')
#   print(soup.prettify())
    proxies_table = soup.find('tbody')

#   Save proxies in the list
    for row in proxies_table.find_all('tr'):
        proxies.append({'ip':   row.find_all('td')[0].string,'port': row.find_all('td')[1].string})
    print(proxies)



if __name__ == '__main__':
  main()