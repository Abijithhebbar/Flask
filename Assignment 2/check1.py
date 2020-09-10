import urllib.request as urllib
import image
import ImageScraper

def getsizes(uri):
    # get file size *and* image size (None if not known)
    file = urllib.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageScraper.scrape_images(URL)
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
            break
    file.close()
    return size, None

print (getsizes("https://i.ytimg.com/vi/b8OT061uxyM/maxresdefault.jpg"))