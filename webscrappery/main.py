from bs4 import BeautifulSoup
import requests

search = input("Enter search value: ")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)
soup = BeautifulSoup(r.text, "html.parser")
"""
f = open("1.html", "w+")

f.write(str(soup.prettify().encode("utf-8")))
"""
results = soup.find("li", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

print("\n")
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        #print("Summary: ", item.find("a").parent.parent.find("p").text)
        parents = item.find("a").parent.parent
        for par in parents:
            print("Parents: ", par)
        print("\n")

