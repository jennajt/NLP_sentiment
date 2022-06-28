# imports
import math
from sysconfig import get_scheme_names
import pandas as pd
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import datetime

# Import data
PATH_TO_CSV = input('Enter path to csv: ')
df = pd.read_csv(f'{PATH_TO_CSV}')
df = pd.DataFrame(df)

class RobertaEmotion():
    def __init__(self):
        '''
        Instantiate model with loaded weights and tokenise pre-trained model.
        '''
        self.task = 'emotion'
        self.link = f"cardiffnlp/twitter-roberta-base-{self.task}"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.link)
        self.tokenizer = AutoTokenizer.from_pretrained(self.link)
        self.labels = None
        print("Model and tokenizer instantiated and loaded")

    def map_labels(self):
        '''
        Load label mapping for selected task.
        '''
        mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{self.task}/mapping.txt"
        with urllib.request.urlopen(mapping_link) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
        self.labels = [row[1] for row in csvreader if len(row) > 1]
        print(self.labels)
        return self.labels

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

        print(f'The first preprocessed tweet is {preprocessed_tweets[0]}')
        return preprocessed_tweets

    def get_scores(self,df,prep_df,append=False):
        '''
        Get scores for model
        '''
        score_list=[]
        dofi = df

        for text in prep_df:
            encoded_input = self.tokenizer(text, return_tensors='pt')
            output = self.model(**encoded_input)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            score_list.append(scores)

        ranking = np.argsort(score_list[0])
        ranking = ranking[::-1]
        results = {"anger": [], "sadness": [], "optimism": [], "joy": []}

        for count, tweet_score in enumerate(score_list):
            for i in range(tweet_score.shape[0]):
                l = self.labels[ranking[i]]
                s = tweet_score[ranking[i]]
                results[f"{l}"].append(np.round(float(s), 4))

        if append == True:

            dofi["joy"] = results["joy"]
            dofi["optimism"] = results["optimism"]
            dofi["anger"] = results["anger"]
            dofi["sadness"] = results["sadness"]

            return dofi

        print(f"The first anger score is {results['anger'][0]}")
        return results

    def combine_processing(self,df):
        '''
        Combines above functions.
        '''

        drop_df = df.drop_duplicates()
        prep_df = self.preprocess(drop_df)
        final_df = self.get_scores(drop_df,prep_df,True)

        dates = pd.to_datetime(final_df["Datetime"]).dt.date
        final_df["only_date"] = dates
        final_df["Text"] = prep_df

        print(f"The first row in the DF is {final_df.head(1)}")
        return final_df

if __name__ == "__main__":
    test = RobertaEmotion()
    test.map_labels()
    test.preprocess(df[:5])
    test.combine_processing(df[:5])
