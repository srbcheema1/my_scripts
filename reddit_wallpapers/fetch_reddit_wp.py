#!/usr/bin/python3
"""
Grabs wallpapers from Reddit
"""
__author__ = 'https://github.com/pit1s'

from os import path, makedirs
from requests import get as reqget
from praw import Reddit

# Name of credentials in praw.ini
reddit = Reddit('WallpaperBot')
subreddit_list = ['spaceporn', 'earthporn', 'pic']
subreddits = [reddit.subreddit(x) for x in subreddit_list]
postlimit = 10

if not path.exists('Wallpapers'):
    makedirs('Wallpapers')

for subreddit in subreddits:
    for post in subreddit.hot(limit=postlimit):
        file = 'Wallpapers\{}_{}.png'.format(post.subreddit, str(int(post.created_utc)))
        if not path.exists(file):
            with open(file, 'wb') as f:
                f.write(reqget(post.url).content)