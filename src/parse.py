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
