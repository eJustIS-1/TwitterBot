import tweepy
import logging
from config import create_api
import json
from tweepy.streaming import Stream

# Sets the logger for fav and retweet bot
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Variables
api = create_api()
userName = "earthquakeBot"
userId = api.get_user(userName).id


# This class uses tweepy API Stream functionality to check twitter user called
# earthquakeBot in order to Fav and Retweet that Bot tweets for showing any earthquakes
# 5.0 or greater when they happen.
class FavRetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id or tweet.user.id is not userId:
            logger.info(f"Could not Process tweet id {tweet.id}")
            return

        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error occured on Fav", exc_info=True)

        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error occured on Ret", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main():
    tweet_listener = FavRetListener(api)
    stream = tweepy.Stream(api.auth, tweet_listener)
    stream.filter(track=["magnitude"])


if __name__ == '__main__':
    main()
