import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
content = tbody.contents # returns a list of all the tags inside the tbody

# traversing the sibling tags (same level of tree)
# print(content[1].previousSibling)
# print(list(content[1].contents))

prices = {}

for tr in content[:10]:
    name, price = tr.contents[2:4]
    crypto_name = name.p.string
    # print(price.a.string)
    crypto_price = price.a.string
    prices[crypto_name] = crypto_price
    
print(prices)