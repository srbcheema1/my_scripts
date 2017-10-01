# Reddit Wallpaper Script
A small python script for grabbing new wallpapers from specified subreddits.

Defaults to the 10 "hot" posts in r/spaceporn, r/earthporn, and r/pic

## Requirements:
- Python 3
- Reddit account 
- Praw (`pip install praw`)

## How to use:

1. Login at https://www.reddit.com/prefs/apps/
2. Create app to get `client_id` and `client_secret`
3. Enter information into `praw.ini`
4. Run the script `python fetch_reddit_wp.py`


## Resources if you get stuck
http://pythonforengineers.com/build-a-reddit-bot-part-1/