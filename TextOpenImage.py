import urllib.request
from PIL import Image

url = 'https://www.tmd.go.th/images/locations/327501.jpg'
image = Image.open(urllib.request.urlopen(url))
width, height = image.size
print (width,height)