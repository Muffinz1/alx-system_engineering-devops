#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
for a given subreddit
returns 0 if the subreddit is wrong
"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subs"""
    reddit_api = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    r = requests.get(reddit_api, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return (0)
    r = r.json()
    if 'data' in r:
        return (r.get('data').get('subscribers'))

    else:
        return (0)
