#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
returns 0 if the subreddit is wrong
"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subs"""
    reddit_sub = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'My-User-Agent'}
    r = requests.get(reddit_sub, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return (0)
    r = r.json()
    if 'data' in r:
        return (r.get('data').get('subscribers'))

    else:
        return (0)
