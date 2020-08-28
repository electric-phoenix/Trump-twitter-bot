import tweepy
import time

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if from_creator(status):
            try:
                # Prints out the tweet
                print(status.text)
                # Saves tweet into a file
                tweetcount += 1
                return True
            except BaseException as e:
                print("Error on_data %s" % str(e))
            return True
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420")
            #returning False in on_error disconnects the stream
            return False
        




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True




tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)

userID = 25073877
usert = "realDonaldTrump"
tweetext = 'Congratulations Jim. It was a great and beautiful event. Well deserved! https://t.co/I4iwvYx3DK'
# stream.filter(follow=["25073877"])

tweetcount=0

tweets = api.user_timeline(screen_name=usert, count=1, include_rts = False, tweet_mode = 'extended')

def check_tweets():
    global tweetext, tweetcount
    for info in tweets[:3]:
            print('Most recent tweet: ', tweetext)
            print('Current count: ', tweetcount)
            print("\n")
            if tweetext != info.full_text:
                tweetext = info.full_text
                tweetcount += 1
                print('New tweet: ', tweetext)
                print('Current count:', tweetcount)
                print("\n")
            else:
                print('No new tweet.... Yet')


while True:
    
    
    if time.strftime("%H") != 0:
        check_tweets()  
        time.sleep(15)
    else:  
        api.update_status('Today Trump has tweeted ',tweetcount,' times')
        tweetcount=0
        






    
    


