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
def delete(api, date, r):
    with open("like.js") as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int(row["tweet_id"])

            try:
                print "Deleting like"
                api.CreateFavorite(status_id=tweet_id)
                api.DestroyFavorite(status_id=tweet_id)
                print tweet_id
                print count
                count += 1
                time.sleep(0.7)

            except twitter.TwitterError, err:
                print "Exception: %s\n" % err.message

print "Number of unliked tweets: %s\n" % count

def error(msg, exit_code=1):
    sys.stderr.write("Error: %s\n" % msg)
    exit(exit_code)

def main():
    parser = argparse.ArgumentParser(description="Delete old tweets.")
    parser.add_argument("-d", dest="date", required=True,
                        help="Delete tweets until this date")
    parser.add_argument("-r", dest="restrict", choices=["reply", "retweet"],
                        help="Restrict to either replies or retweets")

    args = parser.parse_args()

    api = twitter.Api(consumer_key,
                      consumer_secret,
                      access_token_key,
                      access_token_secret)

    delete(api, args.date, args.restrict)


if __name__ == "__main__":
    main()
