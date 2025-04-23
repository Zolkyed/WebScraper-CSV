from parse import fetch_books_data, fetch_yahoo_finance
import pandas as pd
import os

def save_data_to_csv(data, columns, filename):
    df = pd.DataFrame(data, columns=columns)

    directory = os.path.join(os.path.dirname(__file__), '..', 'data')

    if not os.path.exists(directory):
      os.makedirs(directory)

    csv_path = os.path.join(directory, filename)
    df.to_csv(csv_path, index=False)