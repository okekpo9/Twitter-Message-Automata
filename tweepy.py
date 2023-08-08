#  use for sending mrssagesor DM on twitter to different handles
import tweepy
import time
import pandas as pd


lu = pd.read_csv("enter the csv file name containing the twitter handles id  ")
loo = lu['tweet_id']

masage = (
    "enter your message here"
)

auth = tweepy.OAuth1UserHandler(
    "cpuXnZfnMxLUSnLjp9EhWDtuL", "DKFPOdYZwgq3lfoB03aVzmxoexCCz2Hm3s4mP6EquyE8ljGNGP",
    "1147613115665793024-fjRqszazTUpj7BdyiL5NhJrVnYLbSh", "Ik9lfdDFk8rEVxqXSHB60ETcvhxoDGHFq5xVlxzmDbW50"
)

def main():
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # # LIST ID
    list_id = loo
    # Direct Message
    message = masage
    # DON'T CHANGE
    for k in list_id:
        # api.get_user(id=k)
        try:
            api.send_direct_message(k, message)
            print('sending messages succesfully')
            api.wait_on_rate_limit
            time.sleep(15)

        except:
            print('theres an error in sending the message, that escaped me')
            time.sleep(15)
            pass

if __name__ == "__main__":
    main()
