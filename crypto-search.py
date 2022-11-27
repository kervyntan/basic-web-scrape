import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.tbody)