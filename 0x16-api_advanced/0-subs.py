#!/usr/bin/python3
"""
A function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the given subreddit.

    Return:
        Int: the numberof subscribers for a given subreddit.
        If an invalid subreddit is given, returns 0.
    """
    headers = {'User-Agent': 'Amine API Client/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
