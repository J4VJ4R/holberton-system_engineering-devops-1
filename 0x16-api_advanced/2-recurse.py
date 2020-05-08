#!/usr/bin/python3
"""
Script for recurse(subreddit, hot_list=[]) function.
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None.

    Args:
        subreddit (str): The subreddit's name to query
        hot_list (list): The hot list

    Returns:
        Returns a list containing the titles of all hot articles for a given
        subreddit.
        If no titles then None.
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    hdr = {"User-Agent": "My-User-Agent"}
    par = {"count": count, "after": after}

    sub_info = requests.get(url, params=par, headers=hdr,
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot = hot_list + [child.get("data").get("title")
                      for child in sub_info.json()
                      .get("data")
                      .get("children")]

    kind = sub_info.json()
    if not kind.get("data").get("after"):
        return hot

    return recurse(subreddit, hot,
                   kind.get("data").get("count"),
                   kind.get("data").get("after"))
