import requests 
from bs4 import BeautifulSoup

print("enter url : ",end='')
url = input()
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
data = soup.find(class_='inside')
data = soup.find(class_='code')

fout = open("downloaded.txt","w")
fout.write(data.text)
print(data.text)
