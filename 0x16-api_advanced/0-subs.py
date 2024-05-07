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
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
    except (requests.RequestException, ValueError, KeyError):
        subscribers = 0
    
    return subscribers
