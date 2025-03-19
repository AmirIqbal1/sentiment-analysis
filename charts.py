import matplotlib.pyplot as plt

def plot_sentiment(results):
    sentiments = [result['Sentiment'] for result in results]
    positive = sentiments.count('Positive')
    negative = sentiments.count('Negative')
    neutral = sentiments.count('Neutral')

    # Pie Chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [positive, negative, neutral]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.show()

    # Bar Chart
    plt.figure(figsize=(6, 4))
    plt.bar(labels, sizes, color=['green', 'red', 'blue'])
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.show()
