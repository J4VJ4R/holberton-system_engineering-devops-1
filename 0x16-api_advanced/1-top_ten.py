#!/usr/bin/python3
"""
Script for top_ten(subreddit) function.
"""


def top_ten(subreddit):
    """
    Function that queries the Reddit API and  prints the titles of the first 10
    hot posts listed for a given subreddit. If not a valid subreddit, print
    None.

    Args:
        subreddit (str): The subreddit's name to query
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    hdr = {"User-Agent": "My-User-Agent"}

    sub_info = requests.get(url, headers=hdr, allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        for element in sub_info.json().get('data').get('children'):
            print(element.get("data").get("title"))
