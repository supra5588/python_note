from bs4 import BeautifulSoup
import requests

easycamp = requests.get('https://app.easycamp.com.tw').content

soup = BeautifulSoup(easycamp, 'html.parser')

# print(soup.title.text)
print(soup.body.div.attrs)
