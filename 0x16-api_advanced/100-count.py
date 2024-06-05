#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Amine/1.1"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda item: (-item[1], item[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
