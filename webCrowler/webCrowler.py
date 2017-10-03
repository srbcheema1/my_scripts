import time
import bs4
import urllib
import requests

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    #get the HTML of the url, using requests framework and inserting the HTML at Beautiful Soup
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # The div with the main of the article
    content_div = soup.find(class_="mw-parser-output")

    for element in content_div.find_all('p', recursive=False):
        if element.find('a', recursive=False):
            article_link = element.find('a', recursive=False).get('href')
            break

    if not article_link:
        return

    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=30):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!.")
        break
    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    time.sleep(2)
