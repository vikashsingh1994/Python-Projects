import requests

params = {"q": "pizza"}
r = requests.get("http://www.bing.com/search", params = params)
print("Status: ", r.status_code)

print(r.url)
f = open("./page.html", "w+")

# both will work
f.write(str(r.text.encode("utf-8")))

#f.write(str(r.content))