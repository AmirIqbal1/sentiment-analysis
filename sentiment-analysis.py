from textblob import TextBlob

def analyze_sentiment(reviews):
    results = []
    for review in reviews:
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        results.append({'Review': review, 'Sentiment': sentiment, 'Polarity': polarity})
    return results
