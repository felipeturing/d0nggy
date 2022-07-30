'''
Author: Felipe Turing (@felipeturing on GitHub)
Description: Bot is a class that consume the Twitter API v2 used for construct a Twitter Bot.
Base: Twitter API v2 GitHub project @twitterdev
      https://github.com/twitterdev/Twitter-API-v2-sample-code
Version: not yet
'''

from requests_oauthlib import OAuth1Session
import os
import json

class Bot:
    def __init__(self, name: 'Bot name @srt', 
                        twitter_account: 'Twitter bot account',
                        app: 'App Name', 
                        configuration: 'Integer - Twitter Dev level, status, ...') -> 'Bot constructor':
        self.consumer_key = os.environ.get("CONSUMER_KEY")
        self.consumer_secret = os.environ.get("CONSUMER_SECRET")
        self.twitter_account = twitter_account
        self.name = name
        self.app = app
        self.configuration = bin(configuration)[2:]
        print ( "Consumer Key: %s\nTwitter bot account: %s\nConfiguration: %s" % (self.consumer_key, self.twitter_account, self.configuration))

    def get_authorization():
        pass
    def get_access_token():
        pass
    def tweet(self, payload: "Tweet Body") -> "POST Create Tweet":
        pass


# Test
if __name__ == "__main__":
    d0nggy = Bot('D0nggy', 'd0nggy', 'Donggy App', 9812)
