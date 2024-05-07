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

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers)

    returned_data = response.json()

    print(returned_data)

    if "data" in returned_data and "subscribers" in returned_data["data"]:
        return returned_data["data"]["subscribers"]
    else:
        return (0)
