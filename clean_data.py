# imports
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import string
import matplotlib.pyplot as plt
import re
from nltk.stem import WordNetLemmatizer


# If using Google Colab:
    # from google.colab import drive
    # drive.mount('/content/drive')

# Instantiate lists for stopwords and punctuation
nltk.download('stopwords')
string.punctuation
stop_words = stopwords.words('english')
punctuation = [ c for c in string.punctuation ] + [u'\u201c',u'\u201d',u'\u2018',u'\u2019']

# Set file path as a Global Variable
FILE_PATH_NAME = input("Enter file path and name for CSV file")

# Load data
def load_data():
    '''
    Loads a data CSV and returns a dataframe.
    Takes the absolute path of the file and the name of the file as a string.
    '''
    df = pd.read_csv(FILE_PATH_NAME)
    print(f'The shape of the DataFrame is {df.shape}')
    return df

# Process data
def remove_punc(text):
    '''
    Removes the punctuation from a sentence.
    Takes a string and returns a string
    '''
    txt=text
    for punc in punctuation:
        txt = txt.replace(punc, " ")
    txt = txt.lower()
    return txt

def remove_URL_and_HTML(row):
    '''
    Strips the URL from a sentence.
    Takes a string and returns a string
    '''
    row = re.sub(r'http.*$', "", row)
    row = re.sub(r'https.*$', "", row)
    return row

def remove_stopwords(row):
    '''
    Removes stopwords from a sentence.
    Takes a string and returns a string
    '''
    row = word_tokenize(row)
    return ' '.join(w for w in row if not w in stop_words)

def lemmatize(row):
    '''
    Lemmatizes a sentence.
    Takes a string and returns a string
    '''
    lemmatizer = WordNetLemmatizer()
    row = [lemmatizer.lemmatize(word) for word in row.split()]
    return ' '.join(row)

def preprocessing(col):
    '''
    Combines all preprocessing functions into a single function.
    Takes a series of a Dataframe and returns a preprocessed DataFrame.
    '''
    col = col.astype(str)
    punctuation_list = col.apply(remove_punc)
    URL = punctuation_list.apply(remove_URL_and_HTML)
    lem = URL.apply(lemmatize)
    word_tokens = lem.apply(remove_stopwords)
    return word_tokens

# Drop duplicates and turn the dataframe into a clean CSV
def clean(name):
    '''
    Adds the preprocessed column to the dataframe,
    drops duplicates based on the preprocessed column and
    turns the dataframe into a CSV.
    Takes name of the csv file as an input.
    '''
    df = load_data()
    df['preprocessed'] = preprocessing(df['Text'])
    df = df.drop_duplicates(subset='preprocessed', keep='first')
    print(f"The shape of the clean dataframe is {df.shape}")
    return df.to_csv(f"{name}.csv")

if __name__ == "__main__":
    clean('test')
