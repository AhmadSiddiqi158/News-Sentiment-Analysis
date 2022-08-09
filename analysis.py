from unicodedata import name
import nltk
nltk.download('vader_lexicon')
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def translate_scores(score_dict):
    res = ""
    if score_dict['compound'] > 0:
        res = "pos"
    elif score_dict['compound'] < 0:
        res = "neg"
    else:
        res = "neu"
    return res

def analysis(dataframe):
    dataframe["polarity_scores"] = dataframe.text.apply(lambda text: sia.polarity_scores(text))
    dataframe["compound"] = dataframe.polarity_scores.apply(lambda polarity_scores: polarity_scores['compound'])
    dataframe["review"] = dataframe.polarity_scores.apply(lambda polarity_scores: translate_scores(polarity_scores))
    dataframe = dataframe.drop(columns=['polarity_scores','compound'])
    
    sentiments = []
    counts = []
    df = dataframe.value_counts("review")
    for sentiment, count in df.iteritems():
        sentiments.append(sentiment)
        counts.append(count)
    
    plt.subplot(1, 2, 1) # row 1, col 2 index 1
    plt.bar(sentiments, counts)
    plt.title("Sentiment vs Article Count")
    plt.xlabel('Sentiments')
    plt.ylabel('Article count')
    
    plt.subplot(1, 2, 2) # index 2
    plt.pie(counts,labels=sentiments,autopct='%1.1f%%')  
    plt.title("Sentiment Analysis")
    plt.show()

