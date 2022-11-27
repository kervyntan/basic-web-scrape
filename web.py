import requests
from bs4 import BeautifulSoup
# print("Hello World")
with open("index2.html", "r") as f:
    # document passed in as f
    doc = BeautifulSoup(f, "html.parser")
    
# access tags, use doc. the tag (gives the first instance)
# print(doc.h1)
#tag.attrs => gives you attributes in a dictionary
res = doc.find_all("input", type="text")
for r in res:
    r['placeholder'] = "I changed you!"
    
with open("changed.html", "w") as file:
    file.write(str(doc))
#access the html text
# print(doc.h1.string)

#assign value to the html
tag = doc.h1
tag.string = "goodbye"
# print(doc.h1.string)

#find tags
tags = doc.find_all("p") #returns list
# print(tags)

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

"""
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find('strong')
print(strong.string)

"""