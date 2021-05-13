import tweepy
import time

auth = tweepy.OAuthHandler('CODE', 'CODE')
auth.set_access_token('TOKEN', 'TOKEN')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(1000)

search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked that')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break