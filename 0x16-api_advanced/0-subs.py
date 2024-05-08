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

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0 (by /u/MyUsername)'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    except requests.RequestException as e:
        print(f"Error querying subreddit '{subreddit}': {e}")
        return 0
