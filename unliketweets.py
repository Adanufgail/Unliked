#!/usr/bin/env python

import argparse
import csv
import sys
import time
import os
import twitter
from dateutil.parser import parse
import creds

__author__ = "Koen Rouwhorst"
__version__ = "0.1"

import creds
consumer_key = creds.apikeys['consumer_key']
consumer_secret = creds.apikeys['consumer_secret']
access_token_key = creds.apikeys['access_key']
access_token_secret = creds.apikeys['access_secret']
def delete(api):
    with open("like2.js") as file:
        count = 0

        for row in csv.reader(file):
            tweet_id = int(row[0])

            try:
                print "Recreating like"
                api.CreateFavorite(status_id=tweet_id)
                print "Deleting like"
                api.DestroyFavorite(status_id=tweet_id)
                print tweet_id
                print count
                count += 1
                time.sleep(1)

            except twitter.TwitterError, err:
                print "Exception: %s\n" % err.message

        print "Number of unliked tweets: %s\n" % count

def error(msg, exit_code=1):
    sys.stderr.write("Error: %s\n" % msg)
    exit(exit_code)

def main():
    parser = argparse.ArgumentParser(description="Delete old tweets.")

    args = parser.parse_args()

    api = twitter.Api(consumer_key,
                      consumer_secret,
                      access_token_key,
                      access_token_secret)

    delete(api)


if __name__ == "__main__":
    main()
