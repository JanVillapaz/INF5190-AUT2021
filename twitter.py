from datetime import date

import tweepy

API_key = "UBzNgS6oddLhAcCCzVfKthkBu"
API_secret_key = "4hZK96ISUaM5I4wSbA71PrNNGeck1yjA3wNUPHdzQN1cNGj67f"
access_token = "1470227043128385541-8WVm2pFGxzAZCecwOG0oLc8CRGySAI"
access_token_secret = "Dggf1FhJwETXucvfmsDSazlxS3YBYQ9qdXs1RftuiSJvO"


def OAuth():
    try:
        auth = tweepy.OAuthHandler(API_key, API_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None


def send_tweet():
    today = date.today().strftime("%Y/%m/%d, %H:%M:%S")
    oauth = OAuth()
    api = tweepy.API(oauth)
    api.update_status("No updates on : " + today)
