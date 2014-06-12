from twython import Twython

APP_KEY = 'idfhFW2uvKGVMMW5g4vO18wQ2'
APP_SECRET = '49ZAxo2FBip5Hy764c72ljzBcyqXQ5XRj1PFEWoulIwnJaaTv8'
OAUTH_TOKEN = 'idfhFW2uvKGVMMW5g4vO18wQ2'
OAUTH_TOKEN_SECRET = '49ZAxo2FBip5Hy764c72ljzBcyqXQ5XRj1PFEWoulIwnJaaTv8'

def get_tweets(self, keyword):
	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

	res = twitter.search(q='#{0}'.format(keyword), result_type='popular')

	tweets = []

	for r in res['statuses']:
		tweets.append(r['text'])

	return tweets
