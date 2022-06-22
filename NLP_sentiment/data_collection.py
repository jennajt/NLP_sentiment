from ast import Delete
import snscrape.modules.twitter as sntwitter
import pandas as pd

def collect_tweets(keywords, username, name, since="2008-07-28", until="2010-07-28"):
    '''This is a function to scrape tweets from twitter. Takes two lists - keywords and username - , a file name as a string, and dates of query/
    rRturns a csv of relevant tweets'''
    query = " OR ".join(keywords)

    tweets_list = []

    publishers = []
    for paper in username:
        publishers.append("from:" + paper)
    final_pubs = " OR ".join(publishers)

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} {final_pubs} since:{since} until:{until}').get_items()):
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount])
    tweets_list

    df = pd.DataFrame(data=tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Likecount'])

    # print(query)
    # print(final_pubs)
    # print(tweets_list)

    return df.to_csv(f'{name}_tweets.csv')


if __name__ == "__main__":
    collect_tweets(["muslim", "syria", "refugee"], ["DailyMailUK", "TheSun"], "test")
    print('CSV created')
