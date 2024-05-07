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
    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']

    except (requests.RequestException, KeyError):
        subscribers = 0

    return subscribers


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))