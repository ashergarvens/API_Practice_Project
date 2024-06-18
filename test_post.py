import tweepy
import requests

# I was not able to get the actual requests to work but I am able to verify my credientials which is a form of request

api_key = 'wk5iSWwszGioR9afJHEM9zEw4'
api_key_secret = 'ionn1yI4QUiwc2e3Hq1p00C6mi5lcvzYap0n1hZuIRqiSw4lyv'
access_token = '1803160561003155456-eOZ7sJiVDfy4dJzHnl2yVDKXiw37nG'
access_token_secret = 'wO89SkcTheDtP0ATGhpfk4FnVYBY86r1dkM8r75a9pdvR'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJWCuQEAAAAAgeQed0OC1yiCXDHZgBCY5JtrfSE%3DQ1bRktoMdnelC5nS8eRDRoPoV3c9Nukp6JNLftxLfda4map8on'

# Authenticate to Twitter using OAuth 1.1a for user context
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Verify authentication
try:
    user = api.verify_credentials()
    if user:
        print("Authentication OK")
    else:
        print("Failed to authenticate")
except Exception as e:
    print(f"Error during authentication: {e}")

# Fetch the latest tweet from the user's timeline
try:
    tweets = api.home_timeline(count=1)
    latest_tweet = tweets[0].text
    print(f"Latest tweet: {latest_tweet}")
except Exception as e:
    print(f"Error fetching tweets: {e}")

# POST request to another endpoint using the requests library
post_url = 'https://httpbin.org/post'
post_data = {
    'tweet': latest_tweet
}

try:
    response = requests.post(post_url, data=post_data)
    print("POST request status code:", response.status_code)
    print("Response from the POST request:", response.json())
except Exception as e:
    print(f"Error during POST request: {e}")
