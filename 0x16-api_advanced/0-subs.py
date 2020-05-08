#!/usr/bin/python3
"""
Script for number_of_subscribers(subreddit) function.
"""


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    
    Args:
        subreddit (str): The subreddit's name to query

    Returns:
        Queries the Reddit API and returns the number of subscribers to the
        subreddit.
        If is an invalid subreddit returns 0.
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    hdr = {"User-Agent": "My-User-Agent"}

    sub_info = requests.get(url, headers=hdr, allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
