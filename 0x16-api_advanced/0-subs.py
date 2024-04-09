#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
for a given subreddit
returns 0 if the subreddit is wrong
"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subs"""
    reddit_subs = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My Custom User Agent'}
    r = requests.get(reddit_subs, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        subs = r.json()
        return subs['data']['subscribers']
    else:
        return 0
