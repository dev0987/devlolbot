import tweepy
import os
from dotenv import load_dotenv
import pandas

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Twitter requires oAuth2 to access its API
# All keys are stored in .env file
auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), \
                           os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), \
                      os.environ.get('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

jokes = pandas.read_csv(basedir + "/prog_dad_jokes_.csv", header=None, names=['id', 'joke'], index_col=0)

def _get_joke():
    joke_msg = jokes.sample(replace = True).joke.tolist()[0]
    return joke_msg

def tweet_joke():
    joke = _get_joke()
    api.update_status(joke)

if __name__ == "__main__":
    tweet_joke()