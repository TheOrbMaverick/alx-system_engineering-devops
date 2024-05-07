#!/usr/bin/python3
"""
Function that queries the Reddit API and
returns the number of subscribers
"""

import sys
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'u/uniqueagent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']

    except (requests.RequestException, KeyError):
        subscribers = 0

    return subscribers
