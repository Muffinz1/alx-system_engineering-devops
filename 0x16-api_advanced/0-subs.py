#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
for a given subreddit
returns 0 if the subreddit is wrong
"""
import requests


def number_of_subscribers(subreddit):
    """gets the number of subs"""
    reddit_api = ("https://api.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'User-Agent': 'My-User-Agent'}
    r = requests.get(reddit_api, headers=headers, allow_redirects=False)

    if r.status_code >= 300:
        return (0)
    return reddit_api.json().get("data").get("subscribers")
