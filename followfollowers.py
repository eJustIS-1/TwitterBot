import tweepy
import logging
import schedule
import time
from config import create_api
import json

# Sets the logger for followfollowers bot
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Follow the followers who follow the bot
def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                follower.follow()
            except Exception as e:
                logger.error("Error on Follow", exc_info=True)


# Runs the code inside of the infinite loop
def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
