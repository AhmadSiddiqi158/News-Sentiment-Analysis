from newsapi import NewsApiClient
from key import api_key
import pandas as pd
import analysis
import argparse

def get_data(query):
    newsapi = NewsApiClient(api_key)
    data = newsapi.get_everything(q=query, language='en', page_size=100)
    # print(type(data))
    # print(data.keys())
    # print(data['totalResults'])
    articles = data['articles']
    article_titles = []
    for article in articles:
        article_titles.append(article['title'])
    
    return pd.DataFrame(article_titles, columns=['text'])

def clean_data(data):
    return data.drop_duplicates()


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-q', dest='query', help='Search Query', type=str)
        args = parser.parse_args()
    except BaseException as e:
        print("ERROR----Incorrect input: Please verify the input arguments")
        exit(0)

    if args.query is not None:
        df = get_data(args.query)
        df = clean_data(df)
        analysis.analysis(df)
    else:
        print()
        print("********************************************************************")
        print("*** Please enter the topic to perform the sentiment analysis on! ***")
        print("********************************************************************")
        print()

if __name__ == "__main__":
    main()