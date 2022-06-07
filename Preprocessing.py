import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import string
string.punctuation 
print (string.punctuation) 
stop_words = stopwords.words('english')

def preprocessing(df):
    special_characters = df.str.replace('[^\w\s]','')
    URL = special_characters.replace(r'https.*$', "", regex = True)                               
    HTML = [BeautifulSoup(text).get_text() for text in URL]   
    stopwords = [word for word in HTML if word not in (stop_words)]
                                             
    return " ".join(element for element in stopwords)
