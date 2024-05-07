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
    headers = {'User-Agent': 'u/uniqueagent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']

        return subscribers
    
    else:

        return (0)