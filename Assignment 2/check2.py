import requests
from PIL import Image
from io import BytesIO


def get_image_size(url):
    data = requests.get(url).content
    print(data)
    im = Image.open(BytesIO(data))    
    return im.size


if __name__ == "__main__":
    url = "http://localhost:4000/uploads/pic5.png"
    width, height = get_image_size(url)
    print (width, height)