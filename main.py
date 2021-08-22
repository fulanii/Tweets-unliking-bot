import requests
from requests.api import get
from requests.models import Response
import tweepy
from tweepy.api import API

# Authenticate to Twitter for bot to login should always be here
auth = tweepy.OAuthHandler("Paste your Api key here",  # these both auth are basically username and password used by twitter to determine if am who i say i am
    "Paste your Api Secret key here") #auth are the most import tweepy use them to get me in my acount.
auth.set_access_token("Paste your Access Token here", 
    "Paste your Access Token Secret here")
Bearer_token = "Paste your Bearer Token here"

api = tweepy.API(auth) #this needs to be here always for bot to work its the definition of the  api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #this set the authentication credentials and created an api object. You can invoke this object’s methods to do any API call.
User = ("@Your twitter username") # This variable hold the username or the user-id of the user you want to get favorites from This needs to be the users unique username 

print("Getting tweets ids and unliking! ")

# Cursor is the search method this search query will return 20 of the users latest  just like the php api you referenced
for favorite in tweepy.Cursor(api.favorites, id=User).items(1): #in item() you can change the number that's how many ids the bot will get print and unlike
    print(favorite.id)
    api.destroy_favorite(favorite.id)
