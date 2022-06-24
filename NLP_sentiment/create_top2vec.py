# !pip install top2vec==1.0.16
# !pip install tensorflow tensorflow_hub tensorflow_text
# !pip install 'top2vec[sentence_encoders]'
# !pip install 'top2vec[sentence_transformers]'
# !pip install 'top2vec[indexing]'

import pandas as pd
from top2vec import Top2Vec

PATH_TO_CSV = input('Enter path to csv: ')
df = pd.read_csv(f'{PATH_TO_CSV}')
df.sort_values(by=['Datetime'],inplace=True)
df = df.reset_index()

class CreateTop2Vec():
    def __init__(self, workers=-1, speed='fast-learn', min_count=100, embedding_model='universal-sentence-encoder'):
        self.workers = workers
        self.speed = speed
        self.min_count = min_count
        self.embedding_model = embedding_model

    def run_model(self):
        list_tweets_2 = [str(i) for i in df['preprocessed']]
        model = Top2Vec(list_tweets_2, self.workers, self.speed, self.min_count, self.embedding_model)
        print(model.__dict__)
        return model

    def generate_wordcloud(self, model, search_term):
        topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=[search_term], num_topics=5)
        return model.generate_topic_wordcloud(topic_num=topic_nums[0], background_color='white')

if __name__ == "__main__":
    top2vec_practice = CreateTop2Vec(min_count=150)
    top2vec_practice.run_model()
    top2vec_practice.generate_wordcloud(top2vec_practice.run_model(), "migrant")
