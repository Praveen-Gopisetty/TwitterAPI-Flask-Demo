import tweepy
import json


'''
create_connect :: This function establishes and returns connection object 
                  of Twitter API.
'''
def create_connect():
    api_key = "UkpJ3BIZybZXuwK5NteDUMi4S"
    api_secret = "rAozkYum4CR6SdqT74ITJENfOJTqZL2rKzr7zSz1yzBVw7UXLK"
    access_token = "1445460654865862661-NMisnf8Yh59dwkwvkRoByPuiCFyvm8"
    access_secret = "BwN8LP3uJZxiR0OcoGV32InUDg90iXsxzpwKPd5iLB7fY"
    auth = tweepy.OAuthHandler(api_key,api_secret)
    auth.set_access_token(access_token,access_secret)
    api = tweepy.API(auth)
    return api


'''
retrieve_tweets :: This function retrieves the tweets based on search string
                   the user entered.  
'''
def retrieve_tweets(search_term):

    api = create_connect()
    cursor = tweepy.Cursor(api.search_tweets,q=search_term,tweet_mode="extended").items(10)
    tweet_list = [tweet.full_text for tweet in cursor]
    # jsonStr = json.dumps(tweet_list)
    # print(jsonStr)
    return tweet_list

# retrieve_tweets("Dhoni")