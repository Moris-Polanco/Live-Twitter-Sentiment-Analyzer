# -*- coding: utf-8 -*-
"""
@author: Garros

"""
import tweepy as tw
import streamlit as st
import pandas as pd
from transformers import pipeline

self.api_key = 'CXjWqbqODoTLR8hNwe1h352jX'
self.api_key_secret = '5e0c1NR5aQGkHsixpPxxBZulRzxPvRLrMFHI1E3fT0jQnOe7Wh'
self.access_token = '113763054-c0ULFNs4rrXthT9FRnooFDVx8C81HVLZJFYBrctG'
self.access_token_secret = 'ZKyUofCpqNRJMfe28xi3pqOCwJ5Pee4e0psIizBZiHXNK'
auth = tw.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

classifier = pipeline('sentiment-analysis')

st.title('Live Twitter Sentiment Analyzer')
st.markdown('Get the sentiment labels of live tweets!')

def run():
  with st.form(key='Enter name'):
    search_words = st.text_input('Enter the topic for which you want to know the sentiment')
    no_of_tweets = st.number_input('Enter the number of latest tweets for which you want to know the sentiment (maximum 50 tweets)', 0,50,10)
    submit_button = st.form_submit_button(label='Submit')
  if submit_button:
    tweets = tw.Cursor(api.search_tweets,q=search_words,lang="en").items(no_of_tweets)
    tweet_list = [i.text for i in tweets]
    output = [i for i in classifier(tweet_list)]
    labels =[output[i]['label'] for i in range(len(output))]
    df = pd.DataFrame(list(zip(tweet_list, labels)),columns =['Latest '+str(no_of_tweets)+' tweets'+' on '+search_words, 'Sentiment'])
    st.write(df)
 

if __name__=='__main__':
  run()
