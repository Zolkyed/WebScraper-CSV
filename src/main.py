from parse import fetch_books_data, fetch_yahoo_finance
from save_csv import save_data_to_csv
from tqdm import tqdm 

def main():
  books = fetch_books_data()
  stocks = fetch_yahoo_finance()

  save_data_to_csv(books, columns=['Title', 'Price', 'Star Rating'], filename='books.csv')
  save_data_to_csv(stocks, columns=['Name', 'Symbol', 'Price'], filename='stocks.csv')

if __name__ == "__main__":
    main() 