import fetch

def fetch_books_data():
  books = []
  for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    soup = fetch.fetch_page(url)
    ol = soup.find('ol', class_='row')
    articles = ol.find_all('article',class_="product_pod")

    for articles in articles:
      image = articles.find('img')
      title = image.attrs['alt']
      star = articles.find('p')
      star = star['class'][1]
      price = articles.find('p', class_='price_color').text
      books.append([title, price, star])
      
  return books

def fetch_yahoo_finance():
    stock_data = []
    list_stock = ['INTC', 'AMZN', 'NOK', 'GE']
    
    for symbol in list_stock:
        url = f"https://ca.finance.yahoo.com/quote/{symbol}/"
        soup = fetch.fetch_page(url)
        
        price_tag = soup.find('span', class_='base yf-ipw1h0').text
        name_tag = soup.find('h1', class_='yf-xxbei9')
        if name_tag:
           full_name = name_tag.text.strip()
           name, symbol_from_name = full_name.rsplit(' (', 1)
           symbol_from_name = symbol_from_name.rstrip(')')

        stock_data.append([name, symbol, price_tag])
    
    return stock_data