#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Module to provide access to tweets.

Author: Eoin Hurrell <UltimateHurl@gmail.com>
Created: 13-12-27

"""
import oauth2 as oauth
import json
import urllib
import sys
import localSettings


OAUTH_KEY = localSettings.OAUTH_KEY
OAUTH_SECRET = localSettings.OAUTH_SECRET
ACCESS_KEY = localSettings.ACCESS_KEY
ACCESS_SECRET = localSettings.ACCESS_SECRET


def oauth_req(url):
    """Simplified version of twitter's example."""
    consumer = oauth.Consumer(key=OAUTH_KEY, secret=OAUTH_SECRET)
    token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, token)
    resp, content = client.request(url)
    return content


def getSearchResults(term):
    """Search for a term on Twitter.
    Args:
        term   (str):  Search term.
        key    (str):  Oauth key for request.
        secret (str):  Oauth secret for request.

    Returns:
        List of dictionaries, each representing a tweet.

    """
    term = urllib.quote_plus(term)
    searchUrl = 'https://api.twitter.com/1.1/search/tweets.json?q=%s&count=100&result_type=mixed' % (term, )
    search = oauth_req(searchUrl)
    result = json.loads(search)
    return result['statuses']


if __name__ == '__main__':
    term = 'weather'
    if len(sys.argv) > 1:
        term = sys.argv[1]
    statuses = getSearchResults(term)
    for t in statuses:
        print t['user']['screen_name'].encode('utf-8') + ": " + t['text'].encode('utf-8').replace('\n','')
