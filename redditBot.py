import tweepy
import praw
import logging
import schedule
import time
from config import create_api
import json

# Sets the logger for reddit post bot
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Reads Reddit file to get credentials in order to build Reddit Client
redditFile = open("reddit.txt", "r")
credentials_r = redditFile.read().splitlines()

reddit = praw.Reddit(
    client_id=credentials_r[0],
    client_secret=credentials_r[1],
    user_agent="mybot"

)
redditFile.close()


# Takes the hot posts from a subreddit called worldnews and tweets that post
def reddit_post(api):
    posts = reddit.subreddit("worldnews").hot(limit=3)
    for post in posts:
        if (post.stickied == False):
            try:
                api.update_status(
                    post.title + " [ https://www.reddit.com" + post.permalink + " ] ")
                logger.info(f"Sent the Post {post.title}")
            except Exception as e:
                logger.error("Error on Reddit Post", exc_info=True)


def on_error(self, status):
    logger.error(status)


def main():
    api = create_api()
    while True:
        reddit_post(api)
        time.sleep(216000)


if __name__ == '__main__':
    main()
