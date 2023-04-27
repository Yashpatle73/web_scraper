import requests
from bs4 import BeautifulSoup

#url of the webpage you want to scrape 

url = 'https://www.example.com'

#Send an HTTP request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

#for find all links on the webpage
links=soup.find_all('a')

for link in links:
    
# print the href attribute of each link 
    print(links.get('href'),link.text)