import requests

my_data = {"name": "Vikash", "email": "vkumar024@gmail.com"}

r = requests.post("http://www.w3school.com/php/welcome.php", data = my_data)

print("Status: ", r.status_code)

f = open("myhtml.html", "w+")
f.write(r.text)