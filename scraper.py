import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = []
    for review in soup.find_all('div', {'data-hook': 'review'}):
        review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
        reviews.append(review_text)

    # Save reviews to a CSV file
    df = pd.DataFrame(reviews, columns=['Review'])
    df.to_csv('data/reviews.csv', index=False)
    return reviews
