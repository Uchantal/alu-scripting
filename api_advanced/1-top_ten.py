#!/usr/bin/python3
<<<<<<< HEAD
"""DOCS"""
=======
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
>>>>>>> 888ac748658b864726651b54a838dec2a1afb1f6
import requests


def top_ten(subreddit):
<<<<<<< HEAD
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
=======
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])
>>>>>>> 888ac748658b864726651b54a838dec2a1afb1f6
