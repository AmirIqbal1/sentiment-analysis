import tkinter as tk
from tkinter import messagebox, ttk
from scraper import scrape_amazon_reviews
from sentiment_analysis import analyze_sentiment
from charts import plot_sentiment

def start_analysis():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        # Scrape reviews
        reviews = scrape_amazon_reviews(url)
        # Analyze sentiment
        results = analyze_sentiment(reviews)
        # Display results in table
        for result in results:
            table.insert('', 'end', values=(result['Review'], result['Sentiment'], result['Polarity']))
        # Plot charts
        plot_sentiment(results)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# URL Input
tk.Label(root, text="Enter Amazon Product URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Analyze Button
tk.Button(root, text="Analyze", command=start_analysis).pack()

# Results Table
columns = ('Review', 'Sentiment', 'Polarity')
table = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    table.heading(col, text=col)
table.pack()

root.mainloop()
