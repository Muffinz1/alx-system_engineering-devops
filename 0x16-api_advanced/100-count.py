#!/usr/bin/python3
"""
Function to count words in all
top posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, inst={}, after="", child=0):
    """
    The function prints the counts of given words
    which are found in top posts of a given subreddit.
    """
    api = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    params = {
        "after": after,
        "count": child,
        "limit": 100
    }
    response = requests.get(api, headers=headers, params=params,
                            allow_redirects=False)
    try:
        r = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    r = r.get("data")
    after = r.get("after")
    child += r.get("dist")
    for child in r.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if inst.get(word) is None:
                    inst[word] = times
                else:
                    inst[word] += times

    if after is None:
        if len(inst) == 0:
            print("")
            return
        inst = sorted(inst.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in inst]
    else:
        count_words(subreddit, word_list, inst, after, child)
