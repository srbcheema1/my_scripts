import argparse
import requests
from bs4 import BeautifulSoup

def get_code(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    data = soup.find(class_='inside')
    data = soup.find(class_='code')
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Enter url")
    args = parser.parse_args()
    data = get_code(args.url)
    with open("downloaded.txt","w") as fout:
        fout.write(data.text)
        print(data.text)
