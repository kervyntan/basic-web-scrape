from bs4 import BeautifulSoup
import requests

url = "https://reactnative.dev/docs/modal"
request = requests.get(url)
doc = BeautifulSoup(request.text, "html.parser")
items = doc.find_all(class_ = "theme-doc-sidebar-item-link theme-doc-sidebar-item-link-level-2 menu__list-item")

core_components = {}
counter = 0
# to get the text 
print(items[0].contents[0].string)
for item in items:
    text = items[counter].contents[0].string
    core_components[counter] = text
    counter = counter + 1

f = open("corecomponents.txt", "a")
# access each key of the dictionary
for key in core_components:
    f.write(core_components[key])
    f.write("\n")
f.close()