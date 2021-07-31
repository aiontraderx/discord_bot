# import json
import pandas as pd
from picklespick import read_pickle_df
from pytwitterscraper import TwitterScraper
pd.set_option('display.max_columns', 1000, 'display.width', 1000, 'display.max_rows',1000)
import os

class TwitterBot():
    def __init__(self,name):
        self.file_name = 'test.pkl'
        self.tw = TwitterScraper()
        self.name = name

        self.profile = self.tw.get_profile(name=name)
        self.profile_url =self.profile.__dict__['profileurl']
        self.user_id = self.profile.__dict__['id']
        self.follower= self.profile.__dict__['follower']
        self.following= self.profile.__dict__['following']
        self.color = self.profile.__dict__['profile_color']
        # self.id_profile = id_profile
        self.last_id = []
        # tweet_ex['url'] if "url" in tweet_ex else None
        self.data_pickle =  read_pickle_df(self.file_name) if  os.path.exists(self.file_name) else pd.DataFrame()
        print('File Exist',os.path.exists(self.file_name))
        # print(self.data_pickle)
        # self.tweet = {}


    def __str__(self):
            print(f'ID {self.user_id}')
            print(f'NAME {self.name}')
            print('IMG URL:',self.profile_url)
            print(f'Follower {self.follower}: Following {self.following} ')
            print(f'{self.profile.__dict__}')
            print(self.data_pickle)

    def fetch_twitter_post(self,file_name):


        count_x = 2
        tweet_data = self.tw.get_tweets(self.user_id, count=count_x).contents  ### selcetid or 'names '
        print('Tweet Data Raw')
        # print(tweet_data)
        # print(tweet_data[0]) ## Pin Message
        tweet_ex = tweet_data[1] ### Select last tweet

        if not self.data_pickle.empty  : ####self.data['tweet'] or
            print('Data Exiseted')
            tweet = {}
            tweet['id']  =tweet_ex['id']
            # print(self.data_pickle)
            last_order = self.data_pickle['id'].iloc[[-1]]
            last_order =last_order.values[0]
            print('Print Last order',last_order)

            if tweet['id'] != last_order:
                tweet['text'] = tweet_ex['text']
                tweet['like'] = tweet_ex['likes']
                tweet['retweet'] = tweet_ex['retweet']
                tweet['created_at'] = tweet_ex['created_at']
                tweet['hash_tag'] = tweet_ex['hashtags'] if "hashtags" in tweet_ex else None
                tweet['url_link'] = tweet_ex['url'] if "url" in tweet_ex else None
                new_df = pd.DataFrame(tweet)
                print(new_df)
                print('#'*50)

                print('Send To discord')
                print('New DF')
                df = self.data_pickle
                df = pd.concat([df,new_df])
                df.drop_duplicates(keep='first',inplace=True)
                df.to_pickle(file_name)
                return True ,tweet
                #True ,tweet

            if tweet['id'] == last_order:
                id_tweet = tweet['id'] ## convert
                print(f'Last Update ID: {last_order} : Fetch {id_tweet}')
                # False , tweet
                return False ,tweet

        if self.data_pickle.empty: #ot self.data['tweet'] or not

            print('List empty')
            tweet = {}
            tweet['id']  =tweet_ex['id']
            tweet['text'] = tweet_ex['text']
            tweet['like'] = tweet_ex['likes']
            tweet['retweet'] = tweet_ex['retweet']
            tweet['created_at'] = tweet_ex['created_at']
            # print(f'Text {text}\nLike {like} : Retweet {retweet}')
            tweet['hash_tag'] = tweet_ex['hashtags'] if "hashtags" in tweet_ex else None
            tweet['url_link'] = tweet_ex['url'] if "url" in tweet_ex else None
            print(tweet)
            print('DataFrame')
            df= pd.DataFrame(tweet)
            print('Fetch ALL')
            print(df)
            df.to_pickle(self.file_name)
            print('Send To discord')
            print('#'*50)

            return True ,tweet
            # {'id': 1421412567675596812,
            #  'text': 'Tonight we will be proposing the largest farm adjustments yet, this will allow us to follow up with a proposal for… https://t.co/ix4vzg2jMd',
            #  'like': 1454, 'retweet': 251,
            #  'created_at': datetime.datetime(2021, 7, 31, 10, 8, 59, tzinfo=datetime.timezone.utc), 'hash_tag': [],
            #  'url_link': None}
            #

file_name = 'test.pkl'


# michael_saylor pancakeswap
if __name__ == '__main__':
    tw =TwitterBot('michael_saylor')
#     # tw.__str__()
    new_data = tw.fetch_twitter_post(file_name)

