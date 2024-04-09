#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
returns a list containing the titles of all hot articles
for a given subreddit.
If no results are found for the given subreddit
the function should return None.
"""
import requests


def recurse(subreddit, top_list=[]):
    """
    reddit api returns a list that contains the titles of all
    hot articles for a given subreddit
    """
    if type(subreddit) is list:
        sub = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(sub, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    headers = {'User-Agent': 'My-User-Agent'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return (None)
    r = r.json()
    if "data" in r:
        data = r.get("data")
        if not data.get("children"):
            return (top_list)
        for post in data.get("children"):
            top_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (top_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, top_list)
        if top_list[-1] is None:
            del top_list[-1]
        return (top_list)
    else:
        return (None)
