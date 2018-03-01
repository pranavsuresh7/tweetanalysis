import tweepy
import sys
from textblob import TextBlob

consumer_key='vivCTpZCBjRX1JO09yDIKSH59'
consume_secret='Z3SbMv8tJnugfGXUxbwn7qbX3jlsZQS4teDSq4ZCSRwS1ylRsB'

access_consumer='909157367253626880-gjKHvrDFbnJQ6fWKZgDVTe8uCkOCyrS'
access_secret='HiObPKlaTopsVM8pb3oBK7LX0KtYCoWj3dmdf87c12pcG'


auth=tweepy.OAuthHandler(consumer_key,consume_secret)
auth.set_access_token(access_consumer,access_secret)

api=tweepy.API(auth) 

public_tweets=api.search(sys.argv[1])

for tweet in public_tweets:
	print (tweet.text)
analysyis=TextBlob(tweet.text) 

print(analysyis.sentiment)
print("")




