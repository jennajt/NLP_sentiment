# imports
import math
import pandas as pd
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import datetime
import matplotlib.pyplot as plt

df = 


class RobertaEmotion():
    def __init__(self):
        '''
        Instantiate model.
        '''
        self.task = 'emotion'
        self.link = f"cardiffnlp/twitter-roberta-base-{self.task}"

    def load_model(self):
        '''
        Load weights and tokenise pre-trained model based on chosen task.
        '''
        model = AutoModelForSequenceClassification.from_pretrained(self.link)
        tokenizer = AutoTokenizer.from_pretrained(self.link)

    def map_labels(self):
        '''
        Load label mapping for selected task.
        '''
        mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{self.task}/mapping.txt"
        with urllib.request.urlopen(mapping_link) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
        labels = [row[1] for row in csvreader if len(row) > 1]

    def preprocess(self,df):
        '''
        Remove the '@user' and 'http' from the tweets
        '''

        tweets = [str(tweet) for tweet in df["Text"]]
        preprocessed_tweets = []
        for tweet in tweets:
            new_text=[]

            for t in tweet.split(" "):
                t = '@user' if t.startswith('@') and len(t) > 1 else t
                t = 'http' if t.startswith('http') else t
                t = 'http' if '\nhttp' in t else t
                new_text.append(t)

            preprocessed_tweets.append(" ".join(new_text))

        return preprocessed_tweets

    def get_scores(self,df,processed_df,append=False):
        '''
        Get scores for model, append to
        '''
