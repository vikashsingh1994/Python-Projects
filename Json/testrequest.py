import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://purepng.com/public/uploads/large/purepng.com-waterwaterdropslakessea-1411527268114d4naz.png")
print("Status: ", r.status_code)


image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(path, image.format)
except:
    print("Cannot save image")