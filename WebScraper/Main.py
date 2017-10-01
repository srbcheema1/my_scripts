from bs4 import BeautifulSoup
import time
import win32api

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


def scraper():
    # url to scrape
    url = "https://in.bookmyshow.com/buytickets/bairavaa-chennai/movie-chen-ET00046078-MT/20170112"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    # which tag to search for
    # example : table with class : sample => soup.find_all('table',class_="sample")
    tags = soup.find_all('a', class_="__venue-name")

    for tag in tags:
        name = tag.strong.string
        # check if the string what you need is present in the tag
        if (str(name).lower().__contains__("omr")):
            return (name)


runner = True
while (runner):
    result = scraper()
    if (result != None):
        localtime = time.asctime(time.localtime(time.time()))
        print(result + " found at " + localtime)
        win32api.MessageBox(0, 'AGS is opened for booking. \n Booking opened at ' + localtime, 'Book Tickets Now !!')
        runner = False;
    # time before next check (seconds)
    time.sleep(60)
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime + " checking..")
