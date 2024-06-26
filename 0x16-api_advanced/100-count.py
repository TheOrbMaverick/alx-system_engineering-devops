#!/usr/bin/python3
"""
Below is a recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """ A function that returns the count"""
    if counts is None:
        counts = Counter()

    if not word_list:
        return

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] += 1

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items())
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit.")
