from bs4 import BeautifulSoup
import requests

# easycamp = requests.get('https://app.easycamp.com.tw').content
#
# soup = BeautifulSoup(easycamp, 'html.parser')
#
# print(soup.text)


easycamp = requests.get('https://app.easycamp.com.tw').content

soup = BeautifulSoup(easycamp, 'html.parser')

links = soup.findAll('a')

# print(links)

for link in links:
        print(link.string)
