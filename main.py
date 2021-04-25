import tweepy
from tweepy import OAuthHandler
from dotenv import load_dotenv

from tweepy import Stream
from tweepy.streaming import StreamListener

load_dotenv()
 
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_secret = os.getenv('ACCESS_SECRET')
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

## Streaming
# class MyListener(StreamListener):
 
#     def on_data(self, data):
#         try:
#             with open('python.json', 'a') as f:
#                 f.write(data)
#                 return True
#         except BaseException as e:
#             print("Error on_data: %s" % str(e))
#         return True
 
#     def on_error(self, status):
#         print(status)
#         return True
 
# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['#python'])