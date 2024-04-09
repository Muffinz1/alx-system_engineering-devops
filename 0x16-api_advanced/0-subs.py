#!/usr/bin/python3
"""
Reddit api is used to get the number of subs
returns 0 if the subreddit is wrong
"""

import requests


def number_of_subscribers(subreddit):
    """gets the number of subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
