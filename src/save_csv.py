from parse import fetch_books_data
import pandas as pd
import os

books = fetch_books_data()
df = pd.DataFrame(books, columns=['Title','Price','Star Rating'])

directory = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(directory):
    os.makedirs(directory)

csv_path = os.path.join(directory, 'books.csv')
df.to_csv(csv_path, index=False)
