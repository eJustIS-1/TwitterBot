import tweepy
import logging

# Gets the Logger
logger = logging.getLogger()


def create_api():
    # Reads twitter file to get credentials in order to build Twitter Client
    twitterFile = open("twitter.txt", "r")
    credentials_t = twitterFile.read().splitlines()

    # Gets the credentials of API KEYS AND ACCESS TOKENS
    API_KEY = credentials_t[0]
    API_KEY_SECRET = credentials_t[1]
    ACCESS_TOKEN = credentials_t[2]
    ACCESS_TOKEN_SECRET = credentials_t[3]

    # Authentification for Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # Checks and Verifes Credentials
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API created")

    # Closes the read file
    twitterFile.close()

    return api
