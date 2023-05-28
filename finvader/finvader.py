import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .SentiBignomics import *
from .Henry import *


def Merge(dict1, dict2):       # merge two dictionaries
    res = {**dict1, **dict2}
    return res

def finvader(text = 'str',
             indicator = 'str',
             use_sentibignomics: bool= False,
             use_henry: bool= False):

    if use_sentibignomics is True and use_henry is False:
        sentibignomics = lexicon1()
        constant = 0.1  # parameter for tuning classification accurancy
        sentibignomics.update((key, value * constant) for key, value in sentibignomics.items())
        vader1 = SentimentIntensityAnalyzer()
        vader1.lexicon.update(sentibignomics)

        if indicator == "compound":
            sentiment_dict = vader1.polarity_scores(text)
            sentiment = sentiment_dict['compound']

        elif indicator == "neg":
            sentiment_dict = vader1.polarity_scores(text)
            sentiment = sentiment_dict['neg']

        elif indicator == "pos":
            sentiment_dict = vader1.polarity_scores(text)
            sentiment = sentiment_dict['pos']

        elif indicator == "neu":
            sentiment_dict = vader1.polarity_scores(text)
            sentiment = sentiment_dict['neu']

    elif use_henry is True and use_sentibignomics is False:
        henry = lexicon2()
        vader2 = SentimentIntensityAnalyzer()
        vader2.lexicon.update(henry)

        if indicator == "compound":
            sentiment_dict = vader2.polarity_scores(text)
            sentiment = sentiment_dict['compound']

        elif indicator == "neg":
            sentiment_dict = vader2.polarity_scores(text)
            sentiment = sentiment_dict['neg']

        elif indicator == "pos":
            sentiment_dict = vader2.polarity_scores(text)
            sentiment = sentiment_dict['pos']

        elif indicator == "neu":
            sentiment_dict = vader2.polarity_scores(text)
            sentiment = sentiment_dict['neu']


    elif use_henry is True and use_sentibignomics is True:
        sentibignomics = lexicon1()
        constant = 0.1  # parameter for tuning classification accurancy
        sentibignomics.update((key, value * constant) for key, value in sentibignomics.items())
        henry = lexicon2()
        SentiBignomics_Henry = Merge(sentibignomics, henry) # combined lexicon
        vader3 = SentimentIntensityAnalyzer()
        vader3.lexicon.update(SentiBignomics_Henry)

        if indicator == "compound":
            sentiment_dict = vader3.polarity_scores(text)
            sentiment = sentiment_dict['compound']

        elif indicator == "neg":
            sentiment_dict = vader3.polarity_scores(text)
            sentiment = sentiment_dict['neg']

        elif indicator == "pos":
            sentiment_dict = vader3.polarity_scores(text)
            sentiment = sentiment_dict['pos']

        elif indicator == "neu":
            sentiment_dict = vader3.polarity_scores(text)
            sentiment = sentiment_dict['neu']

    return sentiment