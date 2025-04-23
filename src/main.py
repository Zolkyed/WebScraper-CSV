from parse import fetch_books_data, fetch_yahoo_finance
from save_csv import save_data_to_csv
from tqdm import tqdm

def main():
    books = fetch_books_data()
    books_with_progress = tqdm(books, desc="Fetching books", unit="book")
    
    stocks = fetch_yahoo_finance()
    stocks_with_progress = tqdm(stocks, desc="Fetching stocks", unit="stock")
    
    save_data_to_csv(books_with_progress, columns=['Title', 'Price', 'Star Rating'], filename='books.csv')
    save_data_to_csv(stocks_with_progress, columns=['Name', 'Symbol', 'Price'], filename='stocks.csv')

if __name__ == "__main__":
    main()
