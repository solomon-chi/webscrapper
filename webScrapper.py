from bs4 import BeautifulSoup;
import requests;

print("My WebScrapper!!!!!!!!")

url = input("Enter website url: ")

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
