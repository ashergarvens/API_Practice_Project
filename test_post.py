import tweepy

api_key = 'wk5iSWwszGioR9afJHEM9zEw4'
api_key_secret = 'ionn1yI4QUiwc2e3Hq1p00C6mi5lcvzYap0n1hZuIRqiSw4lyv'
access_token = '1803160561003155456-eOZ7sJiVDfy4dJzHnl2yVDKXiw37nG'
access_token_secret = 'wO89SkcTheDtP0ATGhpfk4FnVYBY86r1dkM8r75a9pdvR'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJWCuQEAAAAAgeQed0OC1yiCXDHZgBCY5JtrfSE%3DQ1bRktoMdnelC5nS8eRDRoPoV3c9Nukp6JNLftxLfda4map8on'

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api_v1 = tweepy.API(auth)

# Verify authentication
try:
    user = api_v1.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Fetch user information (commonly accessible)
try:
    user_info = api_v1.get_user(screen_name='TwitterDev')
    print("User Information:")
    print(f"Name: {user_info.name}")
    print(f"Description: {user_info.description}")
    print(f"Followers Count: {user_info.followers_count}")
except Exception as e:
    print(f"Error fetching user information: {e}")

# Post a tweet (commonly accessible)
try:
    tweet = api_v1.update_status("Hello, world! This is a test tweet from the Twitter API.")
    print(f"Successfully posted tweet: {tweet.text}")
except Exception as e:
    print(f"Error posting tweet: {e}")
