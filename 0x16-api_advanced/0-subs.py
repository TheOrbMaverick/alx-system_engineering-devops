#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"user-Agent:" "My User Agent 007"}

    response = requests.get(url, headers=headers)

    returned_data = response.json()

    if "data" in returned_data and "subscribers" in returned_data["data"]:
        return returned_data["data"]["subscribers"]
    else:
        return (0)
