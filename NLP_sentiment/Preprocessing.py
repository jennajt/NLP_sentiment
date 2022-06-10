import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import string
string.punctuation 
print (string.punctuation) 
stop_words = stopwords.words('english')

# -*- coding: utf-8 -*-


punctuation = [ c for c in string.punctuation ] + [u'\u201c',u'\u201d',u'\u2018',u'\u2019']



def remove_punc(text):
    for punc in punctuation:
        text = text.replace(punc, "")
    return text 

def preprocessing(df):
    lower = df.str.lower()
    punctuation_list = lower.apply(remove_punc)
    URL = punctuation_list.replace(r'https.*$', "", regex = True)                               
    HTML = [BeautifulSoup(text).get_text() for text in URL]
    word_tokens = word_tokenize(" ".join(HTML))
    stopwords = [word for word in word_tokens if not word in stop_words]                                         
    return " ".join(element for element in stopwords)

