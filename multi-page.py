from bs4 import BeautifulSoup
import requests
import re #regex

product = input("What product do you want to buy?") 

#create a formatted url based on input
# N=4131 is the filter done by newegg, can observe for other sites
url = f"https://www.newegg.ca/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# returns 
# <span class="list-tool-pagination-text">Page<!-- --> <strong>1<!-- -->/<!-- -->8</strong></span>
# need to get what is in the strong tag (last page)
page_index = doc.find(class_ = "list-tool-pagination-text").strong
# print(page_index)
pages = int(str(page_index).split("/")[-2].split(">")[-1].split("<")[0])
print(pages)

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={product}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    
    items = div.find_all(text=re.compile(product))
    for item in items:
        print(item)