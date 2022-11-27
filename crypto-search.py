import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
content = tbody.contents # returns a list of all the tags inside the tbody

# traversing the sibling tags (same level of tree)
print(content[1].previousSibling)
print(content[1].next_siblings)