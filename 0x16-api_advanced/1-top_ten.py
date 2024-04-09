#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
returns 0 if the subreddit is wrong
"""

import requests


def top_ten(subreddit):
    """Reddit API returns the top 10 posts
    of the subreddit"""

    sub = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    headers = {"User-Agent": "My-User-Agent"}
    r = requests.get(sub, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    response = r.json()
    if 'data' in response:
        for posts in response.get('data').get('children'):
            print(posts.get('data').get('title'))

    else:
        print(None)
