#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all
        hot articles for a given subreddit.
    If no results are found for the given subreddit,
        the function returns None.
    """
    headers = {'User-Agent': 'Amine API Client/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post['data']['title']
                        for post in data['data']['children']])
        if data['data']['after']:
            recurse(subreddit, hot_list, data['data']['after'])
        return hot_list
    else:
        return None
