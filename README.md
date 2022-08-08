# News-Sentiment-Analysis

This project performs VADER sentiment analysis on all the news article's titles of the queried topic.

VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity (strength) of emotion.


## Getting Started

Make sure you have python3 installed.

To install newsapi: ```pip install newsapi-python```

To install newsapi: ```pip install pandas```

To install newsapi: ```pip install matplotlib```

To install natural language tool kit: ```pip install nltk```

To download VADER: ```nltk.download('vader_lexicon')```

<b>Make sure you download VADER using the above comand otherwise the analysis will not work<b>
  
## To run the program
  

```python3 news.py -q <query topic>```
  
### Examples
  
```python3 news.py -q Biden```

```python3 news.py -q "THIS MOVIES WAS AWESOME!!!"```
  
